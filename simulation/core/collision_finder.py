"""
Collision Finder using Birthday Attack

Demonstrates how collisions can be found efficiently using the birthday paradox.
Uses hash tables to store previous hash values for O(1) collision detection.
"""

import time
import random
from typing import Dict, Tuple, Optional, List
from dataclasses import dataclass
from .toy_hash import ToyHashFunction


@dataclass
class CollisionResult:
    """Result of a collision search."""
    found: bool
    input1: bytes
    input2: bytes
    hash_value: int
    attempts: int
    time_elapsed: float
    hash_function: str

    def __str__(self) -> str:
        if not self.found:
            return f"No collision found after {self.attempts} attempts"

        return f"""
Collision Found!
================
Hash Function: {self.hash_function}
Attempts: {self.attempts:,}
Time: {self.time_elapsed:.4f} seconds
Hash Value: 0x{self.hash_value:x} ({self.hash_value})

Input 1: {self.input1}
Input 2: {self.input2}
"""


class BirthdayAttackCollisionFinder:
    """
    Implements birthday attack to find hash collisions.

    The birthday paradox states that in a random set of n samples from
    a space of size N, a collision is expected after approximately sqrt(N)
    samples.
    """

    def __init__(self, hash_function: ToyHashFunction):
        """
        Initialize collision finder.

        Args:
            hash_function: The toy hash function to attack
        """
        self.hash_function = hash_function
        self.hash_table: Dict[int, bytes] = {}
        self.attempts = 0

    def reset(self):
        """Reset the collision finder state."""
        self.hash_table.clear()
        self.attempts = 0

    def find_collision(
        self,
        max_attempts: Optional[int] = None,
        input_generator: str = "random",
        prefix: str = "msg"
    ) -> CollisionResult:
        """
        Find a collision using birthday attack.

        Args:
            max_attempts: Maximum number of attempts (None for unlimited)
            input_generator: Type of input generation ("random", "sequential", "counter")
            prefix: Prefix for generated messages

        Returns:
            CollisionResult object with details of the search
        """
        self.reset()
        start_time = time.time()

        if max_attempts is None:
            # Default: try 10x the expected collision point
            max_attempts = int(10 * (self.hash_function.output_space ** 0.5))

        generator = self._get_input_generator(input_generator, prefix)

        for attempt in range(max_attempts):
            self.attempts = attempt + 1

            # Generate input
            input_data = next(generator)

            # Compute hash
            hash_value = self.hash_function.hash(input_data)

            # Check for collision
            if hash_value in self.hash_table:
                existing_input = self.hash_table[hash_value]
                if existing_input != input_data:
                    # Collision found!
                    time_elapsed = time.time() - start_time
                    return CollisionResult(
                        found=True,
                        input1=existing_input,
                        input2=input_data,
                        hash_value=hash_value,
                        attempts=self.attempts,
                        time_elapsed=time_elapsed,
                        hash_function=str(self.hash_function)
                    )

            # Store hash value
            self.hash_table[hash_value] = input_data

        # No collision found
        time_elapsed = time.time() - start_time
        return CollisionResult(
            found=False,
            input1=b"",
            input2=b"",
            hash_value=0,
            attempts=self.attempts,
            time_elapsed=time_elapsed,
            hash_function=str(self.hash_function)
        )

    def _get_input_generator(self, generator_type: str, prefix: str):
        """Get an input generator based on type."""
        if generator_type == "random":
            return self._random_generator(prefix)
        elif generator_type == "sequential":
            return self._sequential_generator(prefix)
        elif generator_type == "counter":
            return self._counter_generator()
        else:
            raise ValueError(f"Unknown generator type: {generator_type}")

    @staticmethod
    def _random_generator(prefix: str):
        """Generate random inputs."""
        while True:
            random_suffix = random.randint(0, 2**64 - 1)
            yield f"{prefix}_{random_suffix}".encode('utf-8')

    @staticmethod
    def _sequential_generator(prefix: str):
        """Generate sequential inputs."""
        counter = 0
        while True:
            yield f"{prefix}_{counter}".encode('utf-8')
            counter += 1

    @staticmethod
    def _counter_generator():
        """Generate simple counter inputs."""
        counter = 0
        while True:
            yield counter.to_bytes(8, byteorder='big')
            counter += 1

    def theoretical_collision_probability(self, num_samples: int) -> float:
        """
        Calculate theoretical collision probability.

        Uses the approximation: P(collision) ≈ 1 - e^(-n^2 / (2*N))
        where n is number of samples and N is the output space size.

        Args:
            num_samples: Number of hash samples

        Returns:
            Probability of collision (0.0 to 1.0)
        """
        import math
        N = self.hash_function.output_space
        n = num_samples
        exponent = -(n * n) / (2 * N)
        return 1 - math.exp(exponent)

    def expected_attempts_for_collision(self, probability: float = 0.5) -> int:
        """
        Calculate expected number of attempts for a given collision probability.

        Args:
            probability: Desired collision probability (default 0.5 for 50%)

        Returns:
            Expected number of attempts
        """
        import math
        N = self.hash_function.output_space
        # From P ≈ 1 - e^(-n^2/(2N)), solve for n
        # n ≈ sqrt(-2N * ln(1-P))
        return int(math.sqrt(-2 * N * math.log(1 - probability)))


def find_multiple_collisions(
    hash_function: ToyHashFunction,
    num_collisions: int = 5,
    max_attempts_per_collision: Optional[int] = None
) -> List[CollisionResult]:
    """
    Find multiple collisions (resets between each search).

    Args:
        hash_function: Hash function to attack
        num_collisions: Number of collisions to find
        max_attempts_per_collision: Max attempts for each collision search

    Returns:
        List of CollisionResult objects
    """
    finder = BirthdayAttackCollisionFinder(hash_function)
    results = []

    for i in range(num_collisions):
        print(f"Searching for collision {i+1}/{num_collisions}...", end='\r')
        result = finder.find_collision(
            max_attempts=max_attempts_per_collision,
            prefix=f"collision{i}"
        )
        results.append(result)

        if not result.found:
            print(f"\nFailed to find collision {i+1}")
            break

    print()  # New line after progress
    return results


if __name__ == "__main__":
    from .toy_hash import get_toy_hash

    print("Birthday Attack Collision Finder Demo")
    print("=" * 50)

    # Test with 16-bit hash (should find collisions quickly)
    hash_16 = get_toy_hash(16)
    finder = BirthdayAttackCollisionFinder(hash_16)

    print(f"\nAttacking {hash_16}")
    print(f"Output space: {hash_16.output_space:,} possible values")
    print(f"Expected collision after ~{int(hash_16.output_space ** 0.5):,} attempts")

    result = finder.find_collision()
    print(result)

    if result.found:
        # Verify collision
        h1 = hash_16.hash(result.input1)
        h2 = hash_16.hash(result.input2)
        print(f"Verification:")
        print(f"  Hash({result.input1}) = 0x{h1:04x}")
        print(f"  Hash({result.input2}) = 0x{h2:04x}")
        print(f"  Collision: {h1 == h2}")
