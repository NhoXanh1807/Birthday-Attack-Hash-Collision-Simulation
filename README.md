# Birthday Attack Hash Collision Simulation

**Educational demonstration of the birthday paradox applied to cryptographic hash functions**

Course: Cryptography and Network Security
Assignment: Birthday Attack Research and Analysis (Part D - Simulation)

---

## ⚠️ SAFETY NOTICE

**This is an educational tool for demonstrating cryptographic concepts in a safe, controlled environment.**

- ✅ Uses **toy hash functions** with small output sizes (16-32 bits)
- ✅ Runs entirely **locally** in an isolated environment
- ✅ Does **NOT** attack production cryptographic systems
- ✅ Complies with all academic ethics and safety requirements
- ❌ **NOT for use against real-world systems or production hash functions**

This simulation demonstrates the birthday paradox principle that makes collision attacks feasible on weak hash functions, while remaining completely safe and educational.

---

## 📚 Overview

This project implements a comprehensive simulation of birthday attacks on hash functions, demonstrating:

1. **Birthday Paradox Mathematics**: How the collision probability formula `P ≈ 1 - e^(-n²/2N)` applies to hash functions
2. **Collision Finding**: Practical implementation of birthday attack algorithm using hash tables
3. **Probability Analysis**: Empirical measurement and comparison with theoretical predictions
4. **Visualization**: Graphs showing collision probability, attack complexity, and scaling behavior

### Key Features

- **Multiple toy hash implementations** (16, 20, 24, 28, 32-bit outputs)
- **Birthday attack collision finder** with O(√N) expected complexity
- **Probability simulator** running multiple trials to verify theoretical predictions
- **Comprehensive visualizations** including probability curves and complexity analysis
- **CLI interface** for easy experimentation
- **Detailed logging** of all experiments

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/NhoXanh1807/Birthday-Attack-Hash-Collision-Simulation.git
cd Birthday-Attack-Hash-Collision-Simulation

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```bash
# Run interactive demo
python main.py demo

# Find a collision on 16-bit hash
python main.py find --bits 16

# Run probability simulation with 100 trials
python main.py simulate --bits 20 --trials 100

# Generate all visualizations
python main.py visualize --all
```

---

## 📖 Documentation

### Project Structure

```
Birthday-Attack-Hash-Collision-Simulation/
├── simulation/
│   ├── core/                    # Core simulation modules
│   │   ├── toy_hash.py         # Toy hash function implementations
│   │   ├── collision_finder.py # Birthday attack collision finder
│   │   └── probability_simulator.py # Probability analysis
│   ├── utils/                   # Utility modules
│   │   ├── visualization.py    # Plotting and graphing
│   │   └── logger.py           # Experiment logging
│   └── demos/                   # Demonstration scripts
│       ├── demo_collision_finder.py
│       ├── demo_probability.py
│       └── demo_visualization.py
├── results/                     # Output directory
│   ├── graphs/                 # Generated plots
│   └── logs/                   # Experiment logs
├── docs/                        # Documentation
│   └── SAFETY_STATEMENT.md     # Detailed safety information
├── main.py                      # Main CLI interface
├── requirements.txt
└── README.md
```

### Toy Hash Functions

The simulation uses toy hash functions with intentionally small output spaces:

| Bit Size | Output Space | Expected Collisions (√N) |
|----------|--------------|-------------------------|
| 16-bit   | 65,536       | ~256                   |
| 20-bit   | 1,048,576    | ~1,024                 |
| 24-bit   | 16,777,216   | ~4,096                 |
| 28-bit   | 268,435,456  | ~16,384                |
| 32-bit   | 4,294,967,296| ~65,536                |

These hash functions use SHA-256 internally and truncate to the desired bit size, ensuring:
- Cryptographic-quality randomness
- Safe for educational use
- Predictable collision behavior following birthday paradox

---

## 🔬 Examples

### Example 1: Find a Collision

```bash
$ python main.py find --bits 16

Finding Collision: 16-bit Hash
======================================================================
Hash Function: SimpleToyHash-16
Output Space: 65,536
Expected attempts: ~256

Searching for collision...

Collision Found!
================
Hash Function: SimpleToyHash-16
Attempts: 312
Time: 0.0045 seconds
Hash Value: 0x4a7f (19071)

Input 1: b'msg_125'
Input 2: b'msg_287'
```

### Example 2: Probability Simulation

```bash
$ python main.py simulate --bits 16 --trials 100

Running 100 trials with 256 samples each...

Simulation Results for 16-bit Hash
============================================================
Output Space: 65,536 possible hash values
Trials: 100
Samples per Trial: 256

Results:
--------
Collisions Found: 39/100
Empirical Collision Rate: 39.00%
Theoretical Probability: 39.35%
Error: 0.35%

Average Attempts to Collision: 248
Theoretical Expected (50%): 303

Total Time: 1.23 seconds
```

### Example 3: Generate Visualizations

```bash
$ python main.py visualize --all

Generating all visualizations...
Running simulations for hash sizes: 16, 20, 24 bits...
✓ All visualizations generated successfully!

Outputs saved to:
  - results/graphs/probability_16bit.png
  - results/graphs/probability_20bit.png
  - results/graphs/probability_24bit.png
  - results/graphs/attack_complexity.png
  - results/graphs/hash_size_comparison.png
  - results/summary_table.txt
```

---

## 📊 Understanding the Results

### Birthday Paradox Formula

The collision probability after `n` hash operations on an `N`-bit hash function is:

```
P(collision) ≈ 1 - e^(-n²/(2*2^N))
```

At `n = √(2^N)`, the probability reaches approximately **50%**.

### Key Insights

1. **Square Root Complexity**: Birthday attacks require only ~√N operations instead of ~N
2. **Practical Impact**: A 128-bit hash has 2^64 (~18 quintillion) attack complexity, not 2^128
3. **Why 256-bit is Standard**: Modern hash functions use 256+ bits to maintain 2^128+ security

### Visualization Examples

The simulation generates several types of plots:

1. **Probability Curves**: Show how collision probability increases with number of samples
2. **Theoretical vs Empirical**: Validate the birthday paradox formula with measurements
3. **Hash Size Comparison**: Compare collision resistance across different bit sizes
4. **Attack Complexity**: Show exponential growth of attack difficulty

---

## 🎓 Educational Use

### Assignment Deliverables (Part D)

This simulation package includes:

1. ✅ **Source code** - Well-documented Python implementation
2. ✅ **README** - Usage instructions and safety documentation
3. ✅ **Demonstrations** - Multiple demo scripts showing different aspects
4. ✅ **Visualizations** - Graphs and plots illustrating results
5. ✅ **Logs** - Experiment records with timestamps and parameters
6. ✅ **Safety statement** - Clear documentation of isolation and safety measures

### Running Demos for Presentation

For in-class presentation, run the interactive demo:

```bash
python main.py demo
```

Select from:
1. Single collision demonstration (fast, ~1 second)
2. Probability simulation (moderate, ~30 seconds)
3. Hash size comparison (comprehensive, ~2 minutes)
4. Generate visualizations (complete, ~5 minutes)

---

## 🔐 Security & Ethics

### Ethical Guidelines Compliance

This project follows strict ethical guidelines:

- **Isolated Environment**: All experiments run locally without network access
- **Toy Parameters Only**: Uses 16-32 bit hashes, not production cryptographic hashes
- **No Real Attacks**: Does not target real systems, certificates, or documents
- **Educational Purpose**: Designed exclusively for learning cryptographic concepts
- **Transparent Documentation**: Full disclosure of methods and safety measures

### What This Simulation Does NOT Do

❌ Attack production hash functions (MD5, SHA-1, SHA-256, etc.)
❌ Generate collisions for real certificates or signatures
❌ Connect to external systems or networks
❌ Provide tools for malicious use
❌ Include exploitable collision artifacts

### Computational Resources

Typical resource usage:
- **16-bit hash**: ~0.01 seconds, negligible memory
- **20-bit hash**: ~0.1 seconds, <10 MB memory
- **24-bit hash**: ~5 seconds, <100 MB memory
- **28-bit hash**: ~5 minutes, <500 MB memory
- **32-bit hash**: Several hours, <2 GB memory (not recommended for routine demos)

All experiments are bounded and can be interrupted safely.

---

## 📝 Academic References

### Birthday Paradox & Collision Attacks

1. Stallings, W. (2017). *Cryptography and Network Security: Principles and Practice* (7th ed.)
2. Menezes, A., van Oorschot, P., & Vanstone, S. (1996). *Handbook of Applied Cryptography*
3. Yuval, G. (1979). "How to Swindle Rabin." *Cryptologia*, 3(3), 187-191.

### Hash Function Security

4. NIST FIPS 180-4: *Secure Hash Standard (SHS)*
5. Stevens, M., et al. (2017). "The first collision for full SHA-1." *CRYPTO 2017*
6. Wang, X., & Yu, H. (2005). "How to Break MD5 and Other Hash Functions." *EUROCRYPT 2005*

### Best Practices

7. OWASP: *Cryptographic Storage Cheat Sheet*
8. NIST SP 800-57: *Recommendation for Key Management*

---

## 🛠️ Development

### Running Tests

```bash
# Run individual demo scripts
python simulation/demos/demo_collision_finder.py
python simulation/demos/demo_probability.py
python simulation/demos/demo_visualization.py

# Test individual modules
python -m simulation.core.toy_hash
python -m simulation.core.collision_finder
python -m simulation.core.probability_simulator
```

### Extending the Simulation

To add new hash sizes or algorithms:

```python
from simulation.core import ToyHashFunction

# Create custom hash
custom_hash = ToyHashFunction(bit_size=18, name="Custom")

# Use in collision finder
from simulation.core import BirthdayAttackCollisionFinder
finder = BirthdayAttackCollisionFinder(custom_hash)
result = finder.find_collision()
```

---

## 📄 License

This project is created for educational purposes as part of a university assignment.

**Usage Restrictions:**
- ✅ Academic study and research
- ✅ Educational demonstrations
- ✅ Learning cryptographic concepts
- ❌ Commercial use
- ❌ Malicious activities
- ❌ Production system testing

---

## 👥 Team Information

**Course**: Cryptography and Network Security
**Assignment**: Birthday Attack Research and Analysis
**Part**: D - Practical Demonstration / Simulation

---

## 📞 Support & Questions

For questions about this simulation:
1. Review the [Safety Statement](docs/SAFETY_STATEMENT.md)
2. Check the source code documentation
3. Run the demo mode for examples
4. Contact your course instructor

---

## 🎯 Learning Objectives Achieved

By completing this simulation, students demonstrate:

✅ Understanding of birthday paradox mathematics
✅ Knowledge of collision attack complexity (O(2^(n/2)))
✅ Ability to implement cryptographic algorithms safely
✅ Skills in empirical verification of theoretical predictions
✅ Proficiency in data visualization and analysis
✅ Commitment to ethical research practices

---

**Remember**: This is a powerful educational tool. Use it responsibly and ethically! 🎓🔐
