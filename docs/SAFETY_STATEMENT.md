# Safety and Ethics Statement

## Birthday Attack Hash Collision Simulation

**Date**: November 2025
**Course**: Cryptography and Network Security
**Assignment**: Part D - Practical Demonstration/Simulation

---

## Executive Summary

This document provides a comprehensive safety and ethics statement for the Birthday Attack Hash Collision Simulation project. It details the measures taken to ensure the simulation is conducted in a safe, isolated, and ethical manner, in full compliance with academic integrity guidelines and cybersecurity ethics.

**Summary**: This simulation uses toy hash functions with intentionally small output sizes (16-32 bits) in a completely isolated, local environment. It does NOT attack production cryptographic systems and poses no security risk.

---

## 1. Project Scope and Purpose

### 1.1 Educational Objectives

This simulation is designed exclusively for educational purposes to:

- Demonstrate the mathematical principles of the birthday paradox
- Illustrate why collision resistance requires larger hash output sizes
- Provide hands-on experience with cryptographic concepts
- Validate theoretical predictions with empirical measurements
- Teach responsible security research practices

### 1.2 What This Project IS

✅ An educational demonstration of cryptographic principles
✅ A safe, controlled experiment on toy hash functions
✅ A tool for understanding collision attack complexity
✅ A visualization of theoretical probability formulas
✅ An example of ethical security research

### 1.3 What This Project IS NOT

❌ A tool for attacking real cryptographic systems
❌ A method to generate exploitable hash collisions
❌ Software intended for malicious use
❌ A way to compromise production systems
❌ A violation of any security policies or laws

---

## 2. Technical Safety Measures

### 2.1 Toy Hash Functions Only

**Key Safety Feature**: The simulation exclusively uses toy hash functions with small output spaces.

| Hash Type | Bit Size | Output Space | Purpose |
|-----------|----------|--------------|---------|
| Toy Hash  | 16-32 bits | 65K - 4B | Educational demo |
| Production Hash | 256+ bits | 2^256+ | Real security |

**Why This Is Safe**:
- 16-32 bit hashes are NOT used in any production system
- Collision finding is trivial on these small spaces (by design)
- No overlap with real-world cryptographic applications
- Demonstrates principles without security risks

### 2.2 Isolated Local Environment

**Isolation Measures**:

1. **No Network Access**: The simulation does not connect to external systems
2. **No External Data**: Does not download or process third-party data
3. **Local Computation**: All operations run on local machine only
4. **No Distribution**: Does not share collision artifacts externally

**Environment Specifications**:
```
Runtime: Python 3.x (local installation)
Dependencies: matplotlib, numpy (standard scientific libraries)
Network: None required or used
Data Storage: Local filesystem only
```

### 2.3 Bounded Computational Resources

All experiments have safe resource limits:

```python
# Example from collision_finder.py
def find_collision(self, max_attempts: Optional[int] = None):
    if max_attempts is None:
        # Default: 10x expected collision point (bounded)
        max_attempts = int(10 * (self.hash_function.output_space ** 0.5))
```

**Resource Limits**:
- Maximum attempts capped at reasonable values
- Memory usage bounded by hash table size
- Execution time predictable and interruptible
- No unbounded loops or infinite searches

### 2.4 No Production Hash Attacks

**Explicit Protections**:

The code does NOT implement:
- MD5 collision generation
- SHA-1 collision attacks
- Certificate or signature forgery
- Chosen-prefix collision techniques on real hashes
- Any attacks on production cryptographic systems

**Code Safety Example**:
```python
# From toy_hash.py - Safe implementation
def hash(self, data: bytes) -> int:
    """Use SHA256 as base and truncate to toy size."""
    full_hash = hashlib.sha256(data).digest()
    hash_int = int.from_bytes(full_hash[:8], byteorder='big')
    return hash_int & self.mask  # Truncate to 16-32 bits
```

This uses SHA-256 internally for quality randomness, then truncates to toy sizes. It cannot be used to attack real SHA-256.

---

## 3. Ethical Guidelines Compliance

### 3.1 Academic Integrity

This project adheres to university academic integrity policies:

- **Original Work**: All code written specifically for this assignment
- **Proper Attribution**: References to papers and prior research included
- **Honest Reporting**: Results presented accurately without manipulation
- **Transparent Methods**: Full source code and methodology disclosed

### 3.2 Responsible Disclosure

Following responsible security research principles:

- **No Vulnerability Exploitation**: Does not exploit real vulnerabilities
- **No Harmful Tools**: Does not create tools for malicious use
- **Educational Focus**: Designed to teach, not to attack
- **Clear Documentation**: Safety measures fully documented

### 3.3 Compliance with Assignment Requirements

From the assignment specification (Section 6):

> "Do not attempt collisions or attacks on production systems, public services, or third-party data. Experiments must be performed only on local, isolated environments or toy hash functions under your control."

**Our Compliance**:
✅ Uses only toy hash functions under our control
✅ All experiments run locally and isolated
✅ No attacks on production systems or third-party data
✅ Full documentation of isolation measures

### 3.4 Legal Compliance

This simulation complies with all applicable laws:

- **Computer Fraud and Abuse Act (CFAA)**: No unauthorized access to systems
- **Digital Millennium Copyright Act (DMCA)**: No circumvention of protections
- **Local Laws**: Full compliance with jurisdiction-specific regulations
- **University Policies**: Adherence to all institutional guidelines

---

## 4. Risk Assessment

### 4.1 Potential Risks (Assessed)

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Misuse of code | Low | Medium | Clear documentation, educational focus |
| Resource exhaustion | Very Low | Low | Bounded algorithms, limits on execution |
| Academic misconduct | Very Low | High | Original work, proper attribution |
| Unintended consequences | Very Low | Low | Thorough testing, isolated environment |

### 4.2 Risk Mitigation Strategies

1. **Clear Documentation**: README and safety statement prevent misunderstanding
2. **Educational Context**: Assignment framework provides appropriate usage
3. **Technical Limitations**: Toy hashes cannot be used maliciously
4. **Supervised Use**: Project conducted under instructor oversight

### 4.3 Residual Risk Assessment

**Overall Risk Level**: **VERY LOW**

The combination of toy hash functions, isolated environment, educational context, and clear documentation results in negligible security risk. The project poses no threat to any system or individual.

---

## 5. Experiment Methodology

### 5.1 Experimental Design

**Controlled Variables**:
- Hash function type (SimpleToyHash)
- Bit sizes (16, 20, 24, 28, 32)
- Number of trials (typically 50-100)
- Input generation method (sequential, random, counter)

**Measured Variables**:
- Collision attempts required
- Empirical collision probability
- Execution time
- Memory usage

**Controls**:
- Theoretical predictions calculated independently
- Multiple trials for statistical validity
- Reproducible random number generation
- Logged parameters for verification

### 5.2 Data Collection

All experimental data is:
- Generated locally from random inputs
- Stored in local `results/` directory
- Logged with timestamps and parameters
- Never transmitted externally

### 5.3 Reproducibility

The simulation is fully reproducible:

```bash
# Example reproducible run
python main.py find --bits 16
python main.py simulate --bits 16 --trials 100
python main.py visualize --all
```

All results can be verified by rerunning experiments with the same parameters.

---

## 6. Computational Resources

### 6.1 Resource Requirements

**Hardware Used**:
- Standard laptop/desktop computer
- CPU: Any modern processor (no special requirements)
- RAM: 2-8 GB available memory
- Storage: < 100 MB for code and results

**No Special Resources**:
- ❌ No GPU clusters
- ❌ No cloud computing
- ❌ No distributed systems
- ❌ No supercomputers

### 6.2 Execution Time Estimates

| Hash Size | Expected Time | Memory Usage |
|-----------|--------------|--------------|
| 16-bit    | < 1 second   | < 1 MB      |
| 20-bit    | 1-10 seconds | < 10 MB     |
| 24-bit    | 10-60 seconds| < 100 MB    |
| 28-bit    | 1-10 minutes | < 500 MB    |
| 32-bit    | Hours*       | < 2 GB      |

*32-bit demonstrations are optional and not required for assignment

### 6.3 Environmental Impact

Energy consumption is minimal:
- Typical run: < 0.001 kWh
- Complete simulation suite: < 0.01 kWh
- Comparable to watching a short video

---

## 7. Limitations and Disclaimers

### 7.1 Technical Limitations

This simulation:
- Uses simplified toy hash functions
- Operates on small output spaces only
- Does not implement advanced attack techniques
- Cannot be applied to production hash functions

### 7.2 Educational Limitations

This demonstration:
- Shows principles, not production-ready attacks
- Simplifies some cryptographic details
- Focuses on birthday paradox, not all collision attacks
- Does not cover chosen-prefix or other advanced techniques

### 7.3 Legal Disclaimers

**This tool is provided for educational purposes only.**

Users must:
- Use only in educational contexts
- Not attempt attacks on real systems
- Comply with all applicable laws and policies
- Accept full responsibility for their actions

The authors and institution:
- Are not liable for misuse
- Provide no warranty or guarantee
- Reserve right to modify or withdraw tool
- Support only educational and ethical uses

---

## 8. Monitoring and Logging

### 8.1 Experiment Logging

All experiments are logged with:
- Timestamp
- Parameters (hash size, trials, etc.)
- Results (collisions found, time elapsed)
- System information

Example log entry:
```json
{
  "timestamp": "2025-11-14T10:30:00",
  "experiment": "collision_finding",
  "hash_size": 16,
  "attempts": 312,
  "time_elapsed": 0.0045,
  "collision_found": true
}
```

### 8.2 Safety Monitoring

The simulation includes:
- Progress indicators for long-running operations
- Interrupt handling (Ctrl+C to stop)
- Error checking and validation
- Resource usage tracking

### 8.3 Audit Trail

Complete audit trail maintained:
- Source code version control (Git)
- Experiment logs (results/logs/)
- Generated visualizations (results/graphs/)
- Documentation history

---

## 9. Approval and Oversight

### 9.1 Instructor Oversight

This project is conducted under the supervision of:
- Course instructor for Cryptography and Network Security
- University academic integrity office
- Institutional review processes

### 9.2 Peer Review

The simulation has been:
- Reviewed by team members
- Discussed with classmates
- Presented for feedback
- Documented for transparency

### 9.3 Continuous Improvement

We commit to:
- Addressing any safety concerns raised
- Updating documentation as needed
- Responding to feedback
- Maintaining ethical standards

---

## 10. Conclusion

### 10.1 Safety Summary

This Birthday Attack Hash Collision Simulation is safe because:

1. **Toy Hash Functions**: Uses only 16-32 bit hashes, not production hashes
2. **Local Isolation**: Runs entirely on local machine without network access
3. **Educational Purpose**: Designed exclusively for learning
4. **Bounded Resources**: All algorithms have safe resource limits
5. **Transparent Documentation**: Full disclosure of methods and measures
6. **Ethical Compliance**: Adheres to all academic and legal requirements

### 10.2 Educational Value

This simulation provides significant educational value:

- Demonstrates fundamental cryptographic principles
- Validates theoretical predictions empirically
- Teaches responsible security research
- Develops programming and analysis skills
- Prepares students for security careers

### 10.3 Final Statement

**We affirm that**:

This simulation is conducted in a safe, isolated, and ethical manner. It uses only toy hash functions with small output spaces (16-32 bits) for educational demonstration purposes. It does not attack, target, or threaten any production cryptographic system, and poses no security risk to any individual or organization.

All experiments are performed locally on equipment under our control. The simulation complies fully with university policies, academic integrity guidelines, legal requirements, and ethical standards for security research.

We accept full responsibility for the appropriate and ethical use of this educational tool.

---

## 11. Contact and Questions

For questions or concerns about this safety statement:

**Course**: Cryptography and Network Security
**Institution**: [Your University]
**Academic Term**: [Current Term]

---

**Document Version**: 1.0
**Last Updated**: November 14, 2025
**Review Cycle**: Updated as needed

---

## Appendix A: Technical Specifications

### Hash Function Implementation

```python
class ToyHashFunction:
    """Safe toy hash for education only."""

    def __init__(self, bit_size: int):
        assert 1 <= bit_size <= 64, "Safe range"
        self.bit_size = bit_size
        self.output_space = 2 ** bit_size
        self.mask = (1 << bit_size) - 1

    def hash(self, data: bytes) -> int:
        """Cryptographically strong base, truncated to toy size."""
        full_hash = hashlib.sha256(data).digest()
        hash_int = int.from_bytes(full_hash[:8], byteorder='big')
        return hash_int & self.mask
```

### Safety Properties

1. **No weakness exploitation**: Uses SHA-256 internally (secure)
2. **Toy truncation**: Reduces to 16-32 bits (safe, educational)
3. **No real attacks**: Cannot target production systems
4. **Transparent implementation**: Full source code available

---

## Appendix B: Assignment Compliance Checklist

From assignment specification Section 6:

- [x] Experiments performed only on local, isolated environments
- [x] Uses toy hash functions under our control
- [x] No attempts on production systems or public services
- [x] No attempts on third-party data
- [x] Documentation of isolation measures
- [x] Documentation of compute resources
- [x] Explanation of why demonstration is safe
- [x] No distribution of collision artifacts for misuse
- [x] Citations of public research tools (for educational purposes only)
- [x] No inclusion of tooling intended to attack third-party systems

**Compliance Status**: ✅ FULLY COMPLIANT

---

**END OF SAFETY STATEMENT**
