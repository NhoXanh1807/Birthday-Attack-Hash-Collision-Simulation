"""
Visualization utilities for birthday attack simulation results.

Creates graphs and plots to illustrate collision probabilities,
attack complexity, and comparison between theoretical and empirical results.
"""

import math
from typing import List, Dict, Optional, Tuple
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for server environments


def plot_collision_probability_vs_samples(
    bit_size: int,
    max_samples: Optional[int] = None,
    output_file: str = "results/graphs/collision_probability.png"
):
    """
    Plot theoretical collision probability vs number of samples.

    Args:
        bit_size: Size of hash output in bits
        max_samples: Maximum number of samples to plot (default: 3 * sqrt(2^n))
        output_file: Path to save the plot
    """
    output_space = 2 ** bit_size

    if max_samples is None:
        max_samples = int(3 * math.sqrt(output_space))

    # Generate sample counts
    sample_counts = list(range(0, max_samples + 1, max(1, max_samples // 100)))

    # Calculate probabilities
    probabilities = []
    for n in sample_counts:
        if n == 0:
            prob = 0.0
        else:
            exponent = -(n * n) / (2 * output_space)
            prob = 1 - math.exp(exponent)
        probabilities.append(prob)

    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(sample_counts, probabilities, 'b-', linewidth=2)

    # Mark sqrt(N) point (50% collision probability)
    sqrt_n = int(math.sqrt(output_space))
    prob_at_sqrt = 1 - math.exp(-0.5)
    plt.axvline(x=sqrt_n, color='r', linestyle='--', alpha=0.7,
                label=f'√N = {sqrt_n:,} (P ≈ {prob_at_sqrt:.1%})')
    plt.axhline(y=0.5, color='g', linestyle='--', alpha=0.7, label='P = 50%')

    plt.xlabel('Number of Hash Samples', fontsize=12)
    plt.ylabel('Collision Probability', fontsize=12)
    plt.title(f'Birthday Attack: Collision Probability for {bit_size}-bit Hash', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Format y-axis as percentage
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0%}'))

    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Saved plot to {output_file}")


def plot_comparison_theoretical_empirical(
    results: List[Dict],
    bit_size: int,
    output_file: str = "results/graphs/theoretical_vs_empirical.png"
):
    """
    Plot comparison between theoretical and empirical collision probabilities.

    Args:
        results: List of simulation results with 'samples', 'theoretical_prob', 'empirical_prob'
        bit_size: Hash bit size
        output_file: Path to save the plot
    """
    samples = [r['samples'] for r in results]
    theoretical = [r['theoretical_prob'] for r in results]
    empirical = [r['empirical_prob'] for r in results]

    plt.figure(figsize=(10, 6))
    plt.plot(samples, theoretical, 'b-', linewidth=2, label='Theoretical')
    plt.plot(samples, empirical, 'ro-', linewidth=1.5, markersize=6,
             label='Empirical (Measured)', alpha=0.7)

    plt.xlabel('Number of Samples', fontsize=12)
    plt.ylabel('Collision Probability', fontsize=12)
    plt.title(f'Theoretical vs Empirical Collision Probability ({bit_size}-bit Hash)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0%}'))

    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Saved plot to {output_file}")


def plot_hash_size_comparison(
    results_dict: Dict[int, any],
    output_file: str = "results/graphs/hash_size_comparison.png"
):
    """
    Compare collision resistance across different hash sizes.

    Args:
        results_dict: Dictionary mapping bit_size to SimulationResult
        output_file: Path to save the plot
    """
    bit_sizes = sorted(results_dict.keys())
    empirical_rates = [results_dict[size].collision_rate for size in bit_sizes]
    theoretical_rates = [results_dict[size].theoretical_probability for size in bit_sizes]

    x = range(len(bit_sizes))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 6))
    bars1 = ax.bar([i - width/2 for i in x], theoretical_rates, width,
                   label='Theoretical', alpha=0.8)
    bars2 = ax.bar([i + width/2 for i in x], empirical_rates, width,
                   label='Empirical', alpha=0.8)

    ax.set_xlabel('Hash Function Bit Size', fontsize=12)
    ax.set_ylabel('Collision Probability (at √N samples)', fontsize=12)
    ax.set_title('Collision Rates for Different Hash Sizes', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels([f'{size}-bit' for size in bit_sizes])
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')

    # Format y-axis as percentage
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0%}'))

    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Saved plot to {output_file}")


def plot_attack_complexity(
    bit_sizes: List[int],
    output_file: str = "results/graphs/attack_complexity.png"
):
    """
    Plot attack complexity (expected attempts) vs hash size.

    Args:
        bit_sizes: List of hash bit sizes
        output_file: Path to save the plot
    """
    expected_attempts = [int(math.sqrt(2 ** size)) for size in bit_sizes]

    plt.figure(figsize=(10, 6))
    plt.semilogy(bit_sizes, expected_attempts, 'bo-', linewidth=2, markersize=8)

    plt.xlabel('Hash Output Size (bits)', fontsize=12)
    plt.ylabel('Expected Attempts for Collision (log scale)', fontsize=12)
    plt.title('Birthday Attack Complexity: O(2^(n/2))', fontsize=14)
    plt.grid(True, alpha=0.3, which='both')

    # Add annotations for some key points
    for i, (bits, attempts) in enumerate(zip(bit_sizes, expected_attempts)):
        if i % 2 == 0:  # Annotate every other point
            plt.annotate(f'{attempts:,}',
                        xy=(bits, attempts),
                        xytext=(5, 5),
                        textcoords='offset points',
                        fontsize=9)

    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Saved plot to {output_file}")


def create_summary_table(
    results_dict: Dict[int, any],
    output_file: str = "results/summary_table.txt"
):
    """
    Create a text summary table of simulation results.

    Args:
        results_dict: Dictionary mapping bit_size to SimulationResult
        output_file: Path to save the table
    """
    lines = []
    lines.append("=" * 100)
    lines.append("Birthday Attack Simulation Summary")
    lines.append("=" * 100)
    lines.append("")
    lines.append(f"{'Bit Size':<10} {'Output Space':<15} {'√N':<12} "
                f"{'Theoretical':<15} {'Empirical':<15} {'Error':<10}")
    lines.append("-" * 100)

    for bit_size in sorted(results_dict.keys()):
        result = results_dict[bit_size]
        sqrt_n = int(math.sqrt(result.output_space))
        error = abs(result.collision_rate - result.theoretical_probability)

        lines.append(
            f"{bit_size:<10} {result.output_space:<15,} {sqrt_n:<12,} "
            f"{result.theoretical_probability:<15.2%} "
            f"{result.collision_rate:<15.2%} {error:<10.2%}"
        )

    lines.append("=" * 100)
    lines.append("")
    lines.append("Note: All probabilities measured at √N samples")
    lines.append("")

    table_text = "\n".join(lines)
    print(table_text)

    with open(output_file, 'w') as f:
        f.write(table_text)

    print(f"\nSaved summary table to {output_file}")


def plot_all_visualizations(
    bit_sizes: List[int] = [16, 20, 24],
    num_trials: int = 100
):
    """
    Generate all visualization plots.

    Args:
        bit_sizes: List of hash sizes to analyze
        num_trials: Number of trials for empirical measurements
    """
    from ..core import get_toy_hash, ProbabilitySimulator
    from ..core.probability_simulator import compare_hash_sizes

    print("Generating all visualizations...")
    print("=" * 60)

    # 1. Collision probability curves for each hash size
    for bit_size in bit_sizes:
        print(f"\nGenerating probability curve for {bit_size}-bit hash...")
        plot_collision_probability_vs_samples(
            bit_size,
            output_file=f"results/graphs/probability_{bit_size}bit.png"
        )

    # 2. Attack complexity comparison
    print("\nGenerating attack complexity plot...")
    complexity_bit_sizes = list(range(8, 40, 2))
    plot_attack_complexity(
        complexity_bit_sizes,
        output_file="results/graphs/attack_complexity.png"
    )

    # 3. Run simulations and compare theoretical vs empirical
    print("\nRunning simulations for comparison...")
    results_dict = compare_hash_sizes(bit_sizes, trials=num_trials)

    # 4. Hash size comparison
    print("\nGenerating hash size comparison...")
    plot_hash_size_comparison(
        results_dict,
        output_file="results/graphs/hash_size_comparison.png"
    )

    # 5. Summary table
    print("\nGenerating summary table...")
    create_summary_table(
        results_dict,
        output_file="results/summary_table.txt"
    )

    print("\n" + "=" * 60)
    print("All visualizations generated successfully!")
    print("Check the results/graphs/ directory for output files.")


if __name__ == "__main__":
    # Generate all plots
    plot_all_visualizations(bit_sizes=[16, 20, 24], num_trials=50)
