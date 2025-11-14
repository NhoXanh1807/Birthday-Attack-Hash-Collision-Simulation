"""
Toy Hash Functions for Educational Birthday Attack Demonstration

SAFETY NOTE: These are intentionally weak hash functions designed for
educational purposes only. They use small output sizes (16-24-32 bits)
to make collision finding practical in a classroom setting.

DO NOT USE IN PRODUCTION SYSTEMS.
"""

import hashlib
from typing import Callable


class ToyHashFunction:
    """Base class for toy hash functions with configurable bit sizes."""

    def __init__(self, bit_size: int, name: str = "ToyHash"):
        """
        Initialize a toy hash function.

        Args:
            bit_size: Number of bits in the hash output (e.g., 16, 24, 32)
            name: Name identifier for this hash function
        """
        if bit_size <= 0 or bit_size > 64:
            raise ValueError("Bit size must be between 1 and 64")

        self.bit_size = bit_size
        self.name = name
        self.output_space = 2 ** bit_size
        self.mask = (1 << bit_size) - 1

    def hash(self, data: bytes) -> int:
        """
        Compute hash of input data.

        Args:
            data: Input bytes to hash

        Returns:
            Integer hash value in range [0, 2^bit_size - 1]
        """
        # Use SHA256 as a base and truncate to desired bit size
        full_hash = hashlib.sha256(data).digest()
        # Convert first 8 bytes to integer and mask to bit_size
        hash_int = int.from_bytes(full_hash[:8], byteorder='big')
        return hash_int & self.mask

    def hash_string(self, text: str) -> int:
        """Convenience method to hash a string."""
        return self.hash(text.encode('utf-8'))

    def hash_int(self, number: int) -> int:
        """Convenience method to hash an integer."""
        return self.hash(number.to_bytes((number.bit_length() + 7) // 8, byteorder='big'))

    def __str__(self) -> str:
        return f"{self.name}-{self.bit_size}"

    def __repr__(self) -> str:
        return f"ToyHashFunction(bit_size={self.bit_size}, name='{self.name}')"


class SimpleToyHash(ToyHashFunction):
    """Simple toy hash using SHA256 truncation."""

    def __init__(self, bit_size: int):
        super().__init__(bit_size, name="SimpleToyHash")


class ModuloToyHash(ToyHashFunction):
    """Alternative toy hash using modulo operation (even weaker)."""

    def __init__(self, bit_size: int):
        super().__init__(bit_size, name="ModuloToyHash")

    def hash(self, data: bytes) -> int:
        """Hash using simple modulo operation (very weak, for demonstration)."""
        # Sum all bytes and modulo by output space
        byte_sum = sum(data)
        full_hash = hashlib.md5(data).digest()
        hash_int = int.from_bytes(full_hash[:8], byteorder='big')
        return (hash_int + byte_sum) & self.mask


# Predefined common toy hash functions
HASH_16_BIT = SimpleToyHash(16)
HASH_20_BIT = SimpleToyHash(20)
HASH_24_BIT = SimpleToyHash(24)
HASH_28_BIT = SimpleToyHash(28)
HASH_32_BIT = SimpleToyHash(32)

# Dictionary for easy access
PREDEFINED_HASHES = {
    16: HASH_16_BIT,
    20: HASH_20_BIT,
    24: HASH_24_BIT,
    28: HASH_28_BIT,
    32: HASH_32_BIT,
}


def get_toy_hash(bit_size: int) -> ToyHashFunction:
    """
    Get a toy hash function for the specified bit size.

    Args:
        bit_size: Desired output size in bits

    Returns:
        ToyHashFunction instance
    """
    if bit_size in PREDEFINED_HASHES:
        return PREDEFINED_HASHES[bit_size]
    return SimpleToyHash(bit_size)


if __name__ == "__main__":
    # Quick test
    print("Toy Hash Functions Test")
    print("=" * 50)

    test_data = [
        b"hello",
        b"world",
        b"birthday",
        b"attack",
    ]

    for bit_size in [16, 24, 32]:
        hash_func = get_toy_hash(bit_size)
        print(f"\n{hash_func}:")
        print(f"Output space: {hash_func.output_space:,} possible values")
        print(f"Expected collisions after ~{int(hash_func.output_space ** 0.5):,} hashes")

        for data in test_data:
            hash_val = hash_func.hash(data)
            print(f"  {data.decode():12s} -> 0x{hash_val:0{bit_size//4}x} ({hash_val})")
