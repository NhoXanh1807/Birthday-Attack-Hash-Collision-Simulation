#!/usr/bin/env python3
"""
Demo: Visualization of Birthday Attack Results

This demo generates various plots and visualizations to illustrate
collision probabilities and attack complexity.
"""

import sys
sys.path.insert(0, '../..')

from simulation.utils.visualization import (
    plot_collision_probability_vs_samples,
    plot_attack_complexity,
    plot_all_visualizations
)


def demo_probability_curves():
    """Generate probability curves for different hash sizes."""
    print("=" * 70)
    print("Demo: Generating Probability Curves")
    print("=" * 70)

    bit_sizes = [16, 20, 24]

    for bit_size in bit_sizes:
        print(f"\nGenerating curve for {bit_size}-bit hash...")
        plot_collision_probability_vs_samples(
            bit_size=bit_size,
            output_file=f"results/graphs/probability_{bit_size}bit.png"
        )

    print("\n✓ Probability curves generated successfully!")


def demo_complexity_plot():
    """Generate attack complexity visualization."""
    print("\n" + "=" * 70)
    print("Demo: Attack Complexity Visualization")
    print("=" * 70)

    bit_sizes = list(range(8, 40, 2))
    print(f"\nGenerating complexity plot for hash sizes: {bit_sizes[0]}-{bit_sizes[-1]} bits...")

    plot_attack_complexity(
        bit_sizes=bit_sizes,
        output_file="results/graphs/attack_complexity.png"
    )

    print("✓ Complexity plot generated successfully!")


def demo_complete_visualization_suite():
    """Generate complete set of visualizations."""
    print("\n" + "=" * 70)
    print("Demo: Complete Visualization Suite")
    print("=" * 70)

    print("\nGenerating all visualizations with simulations...")
    print("This may take a few minutes...\n")

    plot_all_visualizations(
        bit_sizes=[16, 20, 24],
        num_trials=50  # Reduced for demo speed
    )

    print("\n✓ Complete visualization suite generated!")


if __name__ == "__main__":
    import os

    # Ensure output directories exist
    os.makedirs("results/graphs", exist_ok=True)

    print("\n" + "=" * 70)
    print("BIRTHDAY ATTACK VISUALIZATION DEMONSTRATION")
    print("Educational demonstration - Generating plots and graphs")
    print("=" * 70)

    # Demo 1: Probability curves
    demo_probability_curves()

    # Demo 2: Complexity plot
    demo_complexity_plot()

    # Demo 3: Complete suite (optional - takes longer)
    print("\n" + "=" * 70)
    print("Generate complete visualization suite? (includes simulations)")
    print("This will take several minutes...")
    response = input("Continue? (y/N): ").strip().lower()

    if response == 'y':
        demo_complete_visualization_suite()
    else:
        print("Skipping complete suite. Run manually with:")
        print("  python -c \"from simulation.utils.visualization import plot_all_visualizations; plot_all_visualizations()\"")

    print("\n" + "=" * 70)
    print("Visualization demo completed!")
    print("Check results/graphs/ for output files")
    print("=" * 70)
