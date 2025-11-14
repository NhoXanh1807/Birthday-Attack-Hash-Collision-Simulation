#!/usr/bin/env python3
"""
Demo: Birthday Paradox Probability Analysis

This demo measures empirical collision probabilities and compares them
with theoretical predictions based on the birthday paradox formula.
"""

import sys
sys.path.insert(0, '../..')

from simulation.core import get_toy_hash, ProbabilitySimulator
import math


def demo_single_simulation(bit_size: int = 16, num_trials: int = 100):
    """Demonstrate a single probability simulation."""
    print("=" * 70)
    print(f"Demo: Probability Simulation for {bit_size}-bit Hash")
    print("=" * 70)

    hash_func = get_toy_hash(bit_size)
    simulator = ProbabilitySimulator(hash_func)

    print(f"\nHash Function: {hash_func}")
    print(f"Output Space: {hash_func.output_space:,}")

    # Run simulation
    result = simulator.run_simulation(num_trials=num_trials)
    print(result)

    # Analysis
    error = abs(result.collision_rate - result.theoretical_probability)
    print("Analysis:")
    print("-" * 70)
    print(f"Absolute Error: {error:.4%}")
    print(f"Relative Error: {error / result.theoretical_probability:.2%}")


def demo_scaling_analysis(bit_size: int = 16):
    """Demonstrate how probability scales with number of samples."""
    print("\n" + "=" * 70)
    print(f"Demo: Probability Scaling Analysis ({bit_size}-bit Hash)")
    print("=" * 70)

    hash_func = get_toy_hash(bit_size)
    simulator = ProbabilitySimulator(hash_func)

    sqrt_n = int(math.sqrt(hash_func.output_space))

    # Test different sample counts
    sample_counts = [
        int(sqrt_n * 0.5),
        int(sqrt_n * 0.75),
        sqrt_n,
        int(sqrt_n * 1.5),
        int(sqrt_n * 2.0)
    ]

    print(f"\nTesting with different sample counts (√N = {sqrt_n:,})...")
    results = simulator.run_scaling_analysis(sample_counts, trials_per_count=50)

    # Display results
    print("\n" + "=" * 70)
    print("Results: Collision Probability vs Sample Count")
    print("=" * 70)
    print(f"{'Samples':<12} {'Multiplier':<12} {'Theoretical':<15} "
          f"{'Empirical':<15} {'Difference':<12}")
    print("-" * 70)

    for r in results:
        multiplier = r['samples'] / sqrt_n
        diff = abs(r['theoretical_prob'] - r['empirical_prob'])
        print(f"{r['samples']:<12,} {multiplier:<12.2f} "
              f"{r['theoretical_prob']:<15.2%} {r['empirical_prob']:<15.2%} "
              f"{diff:<12.4%}")


def demo_hash_size_comparison(bit_sizes: list = [12, 16, 20]):
    """Compare collision probabilities across different hash sizes."""
    print("\n" + "=" * 70)
    print("Demo: Comparison Across Hash Sizes")
    print("=" * 70)

    from simulation.core.probability_simulator import compare_hash_sizes

    results = compare_hash_sizes(bit_sizes, trials=50)

    # Summary
    print("\n" + "=" * 70)
    print("Summary: Collision Rates at √N Samples")
    print("=" * 70)
    print(f"{'Bit Size':<10} {'√N':<12} {'Theoretical':<15} "
          f"{'Empirical':<15} {'Match':<8}")
    print("-" * 70)

    for bit_size in bit_sizes:
        result = results[bit_size]
        sqrt_n = int(math.sqrt(result.output_space))
        diff = abs(result.collision_rate - result.theoretical_probability)
        match = "✓" if diff < 0.05 else "✗"

        print(f"{bit_size:<10} {sqrt_n:<12,} "
              f"{result.theoretical_probability:<15.2%} "
              f"{result.collision_rate:<15.2%} {match:<8}")


def demo_theoretical_probabilities(bit_size: int = 16):
    """Show theoretical probabilities at different sample counts."""
    print("\n" + "=" * 70)
    print(f"Demo: Theoretical Birthday Paradox Probabilities ({bit_size}-bit)")
    print("=" * 70)

    hash_func = get_toy_hash(bit_size)
    simulator = ProbabilitySimulator(hash_func)
    sqrt_n = int(math.sqrt(hash_func.output_space))

    print(f"\nOutput Space: {hash_func.output_space:,}")
    print(f"√N = {sqrt_n:,}\n")

    print("Theoretical Collision Probabilities:")
    print("-" * 70)
    print(f"{'Samples':<12} {'As % of √N':<15} {'Probability':<15} {'Description':<20}")
    print("-" * 70)

    test_points = [
        (0.1, "Very low"),
        (0.5, "Half of √N"),
        (0.75, "Three quarters"),
        (1.0, "Exactly √N (50%)"),
        (1.18, "~63% probability"),
        (1.5, "1.5× √N"),
        (2.0, "Double √N"),
        (3.0, "Triple √N"),
    ]

    for multiplier, description in test_points:
        samples = int(sqrt_n * multiplier)
        prob = simulator.calculate_theoretical_probability(samples)
        percent = multiplier * 100
        print(f"{samples:<12,} {percent:<15.1f}% {prob:<15.2%} {description:<20}")


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("BIRTHDAY PARADOX PROBABILITY DEMONSTRATION")
    print("Educational demonstration - Empirical vs Theoretical")
    print("=" * 70)

    # Demo 1: Single simulation
    demo_single_simulation(bit_size=16, num_trials=100)

    # Demo 2: Scaling analysis
    demo_scaling_analysis(bit_size=16)

    # Demo 3: Hash size comparison
    demo_hash_size_comparison(bit_sizes=[12, 16, 20])

    # Demo 4: Theoretical probabilities
    demo_theoretical_probabilities(bit_size=16)

    print("\n" + "=" * 70)
    print("Demo completed successfully!")
    print("=" * 70)
