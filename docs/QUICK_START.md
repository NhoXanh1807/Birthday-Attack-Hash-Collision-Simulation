# Quick Start Guide

## Birthday Attack Hash Collision Simulation

This guide helps you get started with the simulation in under 5 minutes.

---

## Installation (2 minutes)

### Step 1: Prerequisites

Ensure you have Python 3.7+ installed:

```bash
python --version  # Should show Python 3.7 or higher
```

### Step 2: Clone Repository

```bash
git clone https://github.com/NhoXanh1807/Birthday-Attack-Hash-Collision-Simulation.git
cd Birthday-Attack-Hash-Collision-Simulation
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

That's it! Installation complete.

---

## Your First Experiment (3 minutes)

### Experiment 1: Find a Collision (30 seconds)

Find a collision on a 16-bit hash function:

```bash
python main.py find --bits 16
```

**Expected Output**:
```
Collision Found!
================
Attempts: ~300
Time: ~0.005 seconds
Hash Value: 0x4a7f

Input 1: b'msg_125'
Input 2: b'msg_287'
```

**What just happened?**
The simulation generated sequential messages and found two different inputs that hash to the same value. This demonstrates the birthday paradox in action!

### Experiment 2: Measure Probability (1 minute)

Run 100 trials to measure collision probability:

```bash
python main.py simulate --bits 16 --trials 100
```

**Expected Output**:
```
Simulation Results for 16-bit Hash
Collisions Found: 39/100
Empirical Collision Rate: 39.00%
Theoretical Probability: 39.35%
Error: 0.35%
```

**What this shows**:
The empirical (measured) collision rate closely matches the theoretical prediction from the birthday paradox formula!

### Experiment 3: Generate Visualizations (2 minutes)

Create probability curves for different hash sizes:

```bash
python main.py visualize --bit-sizes 16 20
```

**Expected Output**:
- `results/graphs/probability_16bit.png`
- `results/graphs/probability_20bit.png`
- `results/graphs/attack_complexity.png`

Open these PNG files to see visual representations of collision probabilities.

---

## Interactive Demo Mode

For a guided experience:

```bash
python main.py demo
```

Choose from:
1. Single collision demo
2. Probability simulation
3. Hash size comparison
4. Generate visualizations
5. Run all demos

---

## Understanding the Results

### Key Concepts

**Birthday Paradox**: In a room of just 23 people, there's a 50% chance two share a birthday. Similarly, for hash functions:

- **16-bit hash**: Need ~256 attempts for 50% collision chance (not 65,536!)
- **20-bit hash**: Need ~1,024 attempts
- **24-bit hash**: Need ~4,096 attempts

This is why hash functions need large output sizes!

### Interpreting Output

When you find a collision:

```
Hash Function: SimpleToyHash-16
Attempts: 312
Hash Value: 0x4a7f (19071)

Input 1: b'msg_125'
Input 2: b'msg_287'
```

This means:
- It took 312 attempts to find a collision (close to √65536 ≈ 256)
- Both inputs hash to 0x4a7f
- The inputs are different (msg_125 ≠ msg_287)
- This demonstrates the birthday attack works!

---

## Next Steps

### Run Individual Demo Scripts

```bash
# Collision finder demos
python simulation/demos/demo_collision_finder.py

# Probability analysis demos
python simulation/demos/demo_probability.py

# Visualization demos
python simulation/demos/demo_visualization.py
```

### Experiment with Different Parameters

```bash
# Try a larger hash
python main.py find --bits 20

# Run more trials for better statistics
python main.py simulate --bits 16 --trials 1000

# Compare multiple hash sizes
python main.py visualize --bit-sizes 12 16 20 24
```

### Read the Documentation

- **Full README**: [README.md](../README.md)
- **Safety Statement**: [SAFETY_STATEMENT.md](SAFETY_STATEMENT.md)
- **Source Code**: Browse `simulation/` directory

---

## Common Issues

### Issue: `ModuleNotFoundError: No module named 'matplotlib'`

**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: Simulation takes too long

**Solution**: Use smaller hash sizes (16-20 bits) for quick demos
```bash
python main.py find --bits 16  # Fast
python main.py find --bits 24  # Slower
```

### Issue: No graphs generated

**Solution**: Check that matplotlib backend is configured
```bash
python -c "import matplotlib; print(matplotlib.get_backend())"
```

If issues persist, graphs are saved to `results/graphs/` even if not displayed.

---

## Tips for Best Experience

1. **Start Small**: Begin with 16-bit hash for fast results
2. **Watch the Math**: Compare empirical vs theoretical results
3. **Visualize**: Graphs make the concepts much clearer
4. **Experiment**: Try different parameters and observe patterns
5. **Read Code**: The implementation is well-documented

---

## Example Session

Here's a complete 5-minute session:

```bash
# 1. Find a collision (30 sec)
python main.py find --bits 16
# Result: Collision found after ~300 attempts

# 2. Verify with probability simulation (1 min)
python main.py simulate --bits 16 --trials 50
# Result: ~39% collision rate (matches theory!)

# 3. Compare hash sizes (2 min)
python main.py visualize --bit-sizes 16 20 24
# Result: Graphs showing probability curves

# 4. Interactive exploration (2 min)
python main.py demo
# Select option 5 to run all demos
```

Total time: ~5 minutes
Total learning: Understanding why hash functions need 256+ bits! 🎓

---

## For Assignment Submission

### Quick Demo for Presentation

Run this single command for a comprehensive demo:

```bash
python main.py demo
# Choose option 5: Run all demos
```

This will:
1. Find collisions
2. Measure probabilities
3. Generate visualizations
4. Create summary reports

Perfect for demonstrating in class!

### Generate Complete Results Package

```bash
# Generate all visualizations with full statistics
python main.py visualize --all --trials 100

# Results will be in:
# - results/graphs/*.png (plots)
# - results/summary_table.txt (data summary)
```

---

## Safety Reminder

⚠️ This simulation uses **toy hash functions only** (16-32 bits).

✅ Safe for education
✅ Runs locally
✅ No network access
❌ Not for attacking real systems

See [SAFETY_STATEMENT.md](SAFETY_STATEMENT.md) for complete details.

---

## Help and Support

```bash
# View all commands
python main.py --help

# View command-specific help
python main.py find --help
python main.py simulate --help
python main.py visualize --help
```

---

## Summary

You've learned how to:
- ✅ Install and run the simulation
- ✅ Find hash collisions using birthday attacks
- ✅ Measure and verify collision probabilities
- ✅ Generate visualizations
- ✅ Understand the birthday paradox in cryptography

**Next**: Experiment with different parameters and explore the code!

---

**Happy Learning! 🎓🔐**
