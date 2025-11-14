#!/usr/bin/env python3
"""
Demo: Finding Hash Collisions using Birthday Attack

This demo shows how collisions can be found efficiently on small hash functions
using the birthday paradox principle.
"""

import sys
sys.path.insert(0, '../..')

from simulation.core import get_toy_hash, BirthdayAttackCollisionFinder


def demo_single_collision(bit_size: int = 16):
    """Demonstrate finding a single collision."""
    print("=" * 70)
    print(f"Demo: Finding Collision on {bit_size}-bit Hash Function")
    print("=" * 70)

    # Create hash function
    hash_func = get_toy_hash(bit_size)
    print(f"\nHash Function: {hash_func}")
    print(f"Output Space: {hash_func.output_space:,} possible hash values")
    print(f"Expected collision after ~{int(hash_func.output_space ** 0.5):,} attempts")

    # Create collision finder
    finder = BirthdayAttackCollisionFinder(hash_func)

    # Find collision
    print("\nSearching for collision...")
    result = finder.find_collision(input_generator="sequential", prefix="msg")

    # Display results
    print(result)

    if result.found:
        # Verify collision
        h1 = hash_func.hash(result.input1)
        h2 = hash_func.hash(result.input2)

        print("Verification:")
        print("-" * 70)
        print(f"Hash({result.input1.decode()}) = 0x{h1:0{bit_size//4}x}")
        print(f"Hash({result.input2.decode()}) = 0x{h2:0{bit_size//4}x}")
        print(f"Collision confirmed: {h1 == h2}")
        print(f"Inputs are different: {result.input1 != result.input2}")


def demo_multiple_collisions(bit_size: int = 16, num_collisions: int = 3):
    """Demonstrate finding multiple collisions."""
    print("\n" + "=" * 70)
    print(f"Demo: Finding Multiple Collisions on {bit_size}-bit Hash")
    print("=" * 70)

    hash_func = get_toy_hash(bit_size)
    print(f"\nSearching for {num_collisions} collisions...")

    from simulation.core.collision_finder import find_multiple_collisions

    results = find_multiple_collisions(hash_func, num_collisions)

    print(f"\nResults Summary:")
    print("-" * 70)
    for i, result in enumerate(results, 1):
        if result.found:
            print(f"Collision {i}: Found after {result.attempts:,} attempts "
                  f"({result.time_elapsed:.4f}s)")
        else:
            print(f"Collision {i}: Not found")

    # Calculate average
    found_results = [r for r in results if r.found]
    if found_results:
        avg_attempts = sum(r.attempts for r in found_results) / len(found_results)
        avg_time = sum(r.time_elapsed for r in found_results) / len(found_results)
        print(f"\nAverage: {avg_attempts:.0f} attempts, {avg_time:.4f} seconds")


def demo_attack_scaling(bit_sizes: list = [12, 16, 20]):
    """Demonstrate how attack difficulty scales with hash size."""
    print("\n" + "=" * 70)
    print("Demo: Attack Scaling with Hash Size")
    print("=" * 70)

    results = []

    for bit_size in bit_sizes:
        print(f"\nTesting {bit_size}-bit hash...")
        hash_func = get_toy_hash(bit_size)
        finder = BirthdayAttackCollisionFinder(hash_func)

        result = finder.find_collision(prefix=f"test{bit_size}")
        results.append((bit_size, result))

        if result.found:
            print(f"  ✓ Collision found: {result.attempts:,} attempts, "
                  f"{result.time_elapsed:.4f}s")
        else:
            print(f"  ✗ No collision found after {result.attempts:,} attempts")

    # Summary table
    print("\n" + "=" * 70)
    print("Summary: Attack Scaling")
    print("=" * 70)
    print(f"{'Bits':<6} {'Output Space':<15} {'Expected √N':<15} "
          f"{'Actual Attempts':<18} {'Time (s)':<10}")
    print("-" * 70)

    for bit_size, result in results:
        hash_func = get_toy_hash(bit_size)
        sqrt_n = int(hash_func.output_space ** 0.5)
        print(f"{bit_size:<6} {hash_func.output_space:<15,} {sqrt_n:<15,} "
              f"{result.attempts:<18,} {result.time_elapsed:<10.4f}")


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("BIRTHDAY ATTACK COLLISION FINDER DEMONSTRATION")
    print("Educational demonstration - Toy hash functions only")
    print("=" * 70)

    # Demo 1: Single collision
    demo_single_collision(bit_size=16)

    # Demo 2: Multiple collisions
    demo_multiple_collisions(bit_size=16, num_collisions=3)

    # Demo 3: Scaling analysis
    demo_attack_scaling(bit_sizes=[12, 16, 20])

    print("\n" + "=" * 70)
    print("Demo completed successfully!")
    print("=" * 70)
