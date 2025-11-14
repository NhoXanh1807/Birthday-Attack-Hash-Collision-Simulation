#!/usr/bin/env python3
"""
Birthday Attack Hash Collision Simulation - Main CLI

Educational demonstration of the birthday paradox applied to cryptographic
hash functions using toy hash functions with small output sizes.

SAFETY NOTICE:
This simulation uses only toy hash functions (16-32 bits) for educational
purposes. It does NOT attack production hash functions and runs entirely
in a local, isolated environment.
"""

import argparse
import sys
import os
from pathlib import Path

# Add simulation to path
sys.path.insert(0, str(Path(__file__).parent))

from simulation.core import (
    get_toy_hash,
    BirthdayAttackCollisionFinder,
    ProbabilitySimulator
)
from simulation.utils.visualization import (
    plot_collision_probability_vs_samples,
    plot_attack_complexity,
    plot_all_visualizations
)
from simulation.utils.logger import SimulationLogger


def print_banner():
    """Print welcome banner."""
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║     BIRTHDAY ATTACK HASH COLLISION SIMULATION                     ║
║     Educational Demonstration - Cryptography Assignment           ║
╚═══════════════════════════════════════════════════════════════════╝

SAFETY NOTICE: This simulation uses toy hash functions (16-32 bits) only.
It does NOT attack production cryptographic hash functions.
All experiments run in a local, isolated environment.
""")


def cmd_find_collision(args):
    """Find a hash collision using birthday attack."""
    print(f"\n{'='*70}")
    print(f"Finding Collision: {args.bits}-bit Hash")
    print('='*70)

    hash_func = get_toy_hash(args.bits)
    finder = BirthdayAttackCollisionFinder(hash_func)

    print(f"Hash Function: {hash_func}")
    print(f"Output Space: {hash_func.output_space:,}")
    print(f"Expected attempts: ~{int(hash_func.output_space ** 0.5):,}\n")

    result = finder.find_collision(
        max_attempts=args.max_attempts,
        input_generator=args.generator
    )

    print(result)

    if result.found:
        # Verify
        h1 = hash_func.hash(result.input1)
        h2 = hash_func.hash(result.input2)
        print("Verification:")
        print(f"  Hash(input1) = 0x{h1:x}")
        print(f"  Hash(input2) = 0x{h2:x}")
        print(f"  Match: {h1 == h2}")


def cmd_simulate(args):
    """Run probability simulation."""
    print(f"\n{'='*70}")
    print(f"Probability Simulation: {args.bits}-bit Hash")
    print('='*70)

    hash_func = get_toy_hash(args.bits)
    simulator = ProbabilitySimulator(hash_func)

    print(f"Running {args.trials} trials...")
    result = simulator.run_simulation(
        num_trials=args.trials,
        samples_per_trial=args.samples
    )

    print(result)


def cmd_visualize(args):
    """Generate visualizations."""
    print(f"\n{'='*70}")
    print("Generating Visualizations")
    print('='*70)

    os.makedirs("results/graphs", exist_ok=True)

    if args.all:
        print("\nGenerating complete visualization suite...")
        plot_all_visualizations(
            bit_sizes=args.bit_sizes,
            num_trials=args.trials
        )
    else:
        # Generate individual plots
        for bit_size in args.bit_sizes:
            print(f"\nGenerating plots for {bit_size}-bit hash...")
            plot_collision_probability_vs_samples(
                bit_size=bit_size,
                output_file=f"results/graphs/probability_{bit_size}bit.png"
            )

        print("\nGenerating complexity plot...")
        plot_attack_complexity(
            bit_sizes=list(range(8, 40, 2)),
            output_file="results/graphs/attack_complexity.png"
        )

    print("\n✓ Visualizations saved to results/graphs/")


def cmd_demo(args):
    """Run interactive demo."""
    print(f"\n{'='*70}")
    print("Interactive Demo Mode")
    print('='*70)

    print("\nSelect a demonstration:")
    print("  1. Find a single collision (16-bit hash)")
    print("  2. Probability simulation (16-bit hash)")
    print("  3. Hash size comparison (12, 16, 20-bit)")
    print("  4. Generate visualizations")
    print("  5. Run all demos")

    choice = input("\nEnter choice (1-5): ").strip()

    if choice == '1':
        hash_func = get_toy_hash(16)
        finder = BirthdayAttackCollisionFinder(hash_func)
        result = finder.find_collision()
        print(result)

    elif choice == '2':
        hash_func = get_toy_hash(16)
        simulator = ProbabilitySimulator(hash_func)
        result = simulator.run_simulation(num_trials=100)
        print(result)

    elif choice == '3':
        from simulation.core.probability_simulator import compare_hash_sizes
        results = compare_hash_sizes([12, 16, 20], trials=50)
        for bit_size, result in results.items():
            print(f"\n{bit_size}-bit: {result.collision_rate:.2%} collision rate")

    elif choice == '4':
        os.makedirs("results/graphs", exist_ok=True)
        plot_all_visualizations(bit_sizes=[16, 20, 24], num_trials=50)

    elif choice == '5':
        print("\nRunning all demos...")
        # Run collision finder
        print("\n1. Collision Finder Demo:")
        hash_func = get_toy_hash(16)
        finder = BirthdayAttackCollisionFinder(hash_func)
        result = finder.find_collision()
        print(f"   Collision found after {result.attempts} attempts")

        # Run probability simulation
        print("\n2. Probability Simulation Demo:")
        simulator = ProbabilitySimulator(hash_func)
        result = simulator.run_simulation(num_trials=50)
        print(f"   Empirical: {result.collision_rate:.2%}, "
              f"Theoretical: {result.theoretical_probability:.2%}")

        # Generate visualizations
        print("\n3. Generating visualizations...")
        os.makedirs("results/graphs", exist_ok=True)
        plot_all_visualizations(bit_sizes=[16, 20], num_trials=30)

        print("\n✓ All demos completed!")

    else:
        print("Invalid choice!")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Birthday Attack Hash Collision Simulation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s find --bits 16
  %(prog)s simulate --bits 20 --trials 100
  %(prog)s visualize --all
  %(prog)s demo

Safety Notice:
  This tool uses toy hash functions only (16-32 bits).
  It does NOT attack production cryptographic systems.
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Command to run')

    # Find collision command
    parser_find = subparsers.add_parser('find', help='Find hash collision')
    parser_find.add_argument('--bits', type=int, default=16,
                            help='Hash output size in bits (default: 16)')
    parser_find.add_argument('--max-attempts', type=int, default=None,
                            help='Maximum attempts (default: 10*sqrt(N))')
    parser_find.add_argument('--generator', default='sequential',
                            choices=['random', 'sequential', 'counter'],
                            help='Input generator type')
    parser_find.set_defaults(func=cmd_find_collision)

    # Simulate command
    parser_sim = subparsers.add_parser('simulate', help='Run probability simulation')
    parser_sim.add_argument('--bits', type=int, default=16,
                           help='Hash output size in bits (default: 16)')
    parser_sim.add_argument('--trials', type=int, default=100,
                           help='Number of trials (default: 100)')
    parser_sim.add_argument('--samples', type=int, default=None,
                           help='Samples per trial (default: sqrt(N))')
    parser_sim.set_defaults(func=cmd_simulate)

    # Visualize command
    parser_viz = subparsers.add_parser('visualize', help='Generate visualizations')
    parser_viz.add_argument('--bit-sizes', type=int, nargs='+', default=[16, 20, 24],
                           help='Hash sizes to visualize (default: 16 20 24)')
    parser_viz.add_argument('--trials', type=int, default=50,
                           help='Trials for simulations (default: 50)')
    parser_viz.add_argument('--all', action='store_true',
                           help='Generate complete visualization suite')
    parser_viz.set_defaults(func=cmd_visualize)

    # Demo command
    parser_demo = subparsers.add_parser('demo', help='Run interactive demo')
    parser_demo.set_defaults(func=cmd_demo)

    args = parser.parse_args()

    print_banner()

    if args.command is None:
        parser.print_help()
        return

    # Execute command
    args.func(args)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
