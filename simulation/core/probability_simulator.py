"""
Birthday Attack Probability Simulator

Runs multiple trials to empirically measure collision probabilities
and compare them with theoretical predictions.
"""

import time
import math
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import random
from .toy_hash import ToyHashFunction
from .collision_finder import BirthdayAttackCollisionFinder


@dataclass
class SimulationResult:
    """Results from a probability simulation."""
    bit_size: int
    output_space: int
    num_trials: int
    samples_per_trial: int
    collisions_found: int
    collision_rate: float
    theoretical_probability: float
    average_attempts_to_collision: float
    theoretical_expected_attempts: int
    total_time: float

    def __str__(self) -> str:
        return f"""
Simulation Results for {self.bit_size}-bit Hash
{'=' * 60}
Output Space: {self.output_space:,} possible hash values
Trials: {self.num_trials}
Samples per Trial: {self.samples_per_trial}

Results:
--------
Collisions Found: {self.collisions_found}/{self.num_trials}
Empirical Collision Rate: {self.collision_rate:.2%}
Theoretical Probability: {self.theoretical_probability:.2%}
Error: {abs(self.collision_rate - self.theoretical_probability):.2%}

Average Attempts to Collision: {self.average_attempts_to_collision:.0f}
Theoretical Expected (50%): {self.theoretical_expected_attempts}

Total Time: {self.total_time:.2f} seconds
"""


class ProbabilitySimulator:
    """Simulates birthday attacks to measure empirical collision probabilities."""

    def __init__(self, hash_function: ToyHashFunction):
        """
        Initialize simulator.

        Args:
            hash_function: The toy hash function to simulate
        """
        self.hash_function = hash_function

    def calculate_theoretical_probability(self, num_samples: int) -> float:
        """
        Calculate theoretical collision probability using birthday paradox formula.

        P(collision) ≈ 1 - e^(-n^2 / (2*N))

        Args:
            num_samples: Number of hash samples

        Returns:
            Probability of at least one collision
        """
        N = self.hash_function.output_space
        n = num_samples
        exponent = -(n * n) / (2 * N)
        return 1 - math.exp(exponent)

    def calculate_expected_attempts(self, probability: float = 0.5) -> int:
        """
        Calculate expected attempts for given collision probability.

        Args:
            probability: Target probability (default 0.5)

        Returns:
            Expected number of attempts
        """
        N = self.hash_function.output_space
        return int(math.sqrt(-2 * N * math.log(1 - probability)))

    def run_single_trial(self, num_samples: int) -> Tuple[bool, int]:
        """
        Run a single trial to check for collisions.

        Args:
            num_samples: Number of samples to generate

        Returns:
            Tuple of (collision_found, attempts_until_collision)
        """
        seen_hashes = set()

        for i in range(num_samples):
            # Generate random input
            random_input = random.randint(0, 2**64 - 1).to_bytes(8, byteorder='big')
            hash_value = self.hash_function.hash(random_input)

            if hash_value in seen_hashes:
                return True, i + 1

            seen_hashes.add(hash_value)

        return False, num_samples

    def run_simulation(
        self,
        num_trials: int = 100,
        samples_per_trial: Optional[int] = None
    ) -> SimulationResult:
        """
        Run multiple trials to measure empirical collision probability.

        Args:
            num_trials: Number of independent trials to run
            samples_per_trial: Number of samples per trial (default: sqrt(N))

        Returns:
            SimulationResult object
        """
        if samples_per_trial is None:
            # Default: use sqrt(N) for ~50% collision probability
            samples_per_trial = int(math.sqrt(self.hash_function.output_space))

        print(f"Running {num_trials} trials with {samples_per_trial} samples each...")
        start_time = time.time()

        collisions_found = 0
        attempts_list = []

        for trial in range(num_trials):
            if (trial + 1) % max(1, num_trials // 10) == 0:
                print(f"Progress: {trial + 1}/{num_trials} trials", end='\r')

            found, attempts = self.run_single_trial(samples_per_trial)
            if found:
                collisions_found += 1
                attempts_list.append(attempts)

        print()  # New line after progress

        total_time = time.time() - start_time
        collision_rate = collisions_found / num_trials
        theoretical_prob = self.calculate_theoretical_probability(samples_per_trial)
        avg_attempts = sum(attempts_list) / len(attempts_list) if attempts_list else 0
        expected_attempts = self.calculate_expected_attempts(0.5)

        return SimulationResult(
            bit_size=self.hash_function.bit_size,
            output_space=self.hash_function.output_space,
            num_trials=num_trials,
            samples_per_trial=samples_per_trial,
            collisions_found=collisions_found,
            collision_rate=collision_rate,
            theoretical_probability=theoretical_prob,
            average_attempts_to_collision=avg_attempts,
            theoretical_expected_attempts=expected_attempts,
            total_time=total_time
        )

    def run_scaling_analysis(
        self,
        sample_counts: List[int],
        trials_per_count: int = 50
    ) -> List[Dict]:
        """
        Run simulations with varying sample counts to show scaling behavior.

        Args:
            sample_counts: List of sample counts to test
            trials_per_count: Number of trials for each sample count

        Returns:
            List of result dictionaries
        """
        results = []

        for num_samples in sample_counts:
            print(f"\nTesting with {num_samples} samples...")
            result = self.run_simulation(trials_per_count, num_samples)

            results.append({
                'samples': num_samples,
                'empirical_prob': result.collision_rate,
                'theoretical_prob': result.theoretical_probability,
                'collisions_found': result.collisions_found,
                'trials': trials_per_count
            })

        return results


def compare_hash_sizes(
    bit_sizes: List[int],
    trials: int = 100
) -> Dict[int, SimulationResult]:
    """
    Compare collision probabilities across different hash sizes.

    Args:
        bit_sizes: List of bit sizes to test
        trials: Number of trials per bit size

    Returns:
        Dictionary mapping bit_size to SimulationResult
    """
    from .toy_hash import get_toy_hash

    results = {}

    for bit_size in bit_sizes:
        print(f"\n{'='*60}")
        print(f"Testing {bit_size}-bit hash function")
        print('='*60)

        hash_func = get_toy_hash(bit_size)
        simulator = ProbabilitySimulator(hash_func)

        # Use sqrt(N) samples for fair comparison
        samples = int(math.sqrt(hash_func.output_space))
        result = simulator.run_simulation(trials, samples)

        results[bit_size] = result
        print(result)

    return results


if __name__ == "__main__":
    from .toy_hash import get_toy_hash

    print("Birthday Attack Probability Simulator")
    print("=" * 60)

    # Test with 16-bit hash
    hash_func = get_toy_hash(16)
    simulator = ProbabilitySimulator(hash_func)

    print(f"\nHash Function: {hash_func}")
    print(f"Output Space: {hash_func.output_space:,}")
    print(f"Expected collisions after ~{int(hash_func.output_space ** 0.5):,} samples")

    # Run simulation
    result = simulator.run_simulation(num_trials=100)
    print(result)

    # Show theoretical probabilities at different sample counts
    print("\nTheoretical Collision Probabilities:")
    print("-" * 40)
    sqrt_n = int(math.sqrt(hash_func.output_space))
    for multiplier in [0.5, 1.0, 1.5, 2.0]:
        samples = int(sqrt_n * multiplier)
        prob = simulator.calculate_theoretical_probability(samples)
        print(f"  {samples:6,} samples: {prob:6.2%}")
