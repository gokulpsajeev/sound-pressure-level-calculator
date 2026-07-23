
## Overview

This Python application calculates the Sound Pressure Level (SPL) in decibels from an input RMS sound pressure using the standard reference pressure of 20 µPa.

The project demonstrates the application of acoustic engineering principles and Python programming for basic aeroacoustics calculations.

---

## Features

- Calculate Sound Pressure Level (SPL)
- Uses standard acoustic equation
- Simple command-line interface
- Beginner-friendly Python implementation

---

## Theory

The Sound Pressure Level is calculated using:

SPL = 20 × log10(P / Pref)

where:

- P = RMS Sound Pressure (Pa)
- Pref = 20 × 10⁻⁶ Pa (Reference Pressure)

---

## Requirements

- Python 3.10+
- No external libraries required

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/sound-pressure-level-calculator.git
```

Run the program

```bash
python spl_calculator.py
```

---

## Example

Input

```
Enter RMS Sound Pressure (Pa): 0.5
```

Output

```
Input Pressure : 0.500000 Pa
SPL            : 87.96 dB
```

---

## Applications

- Aeroacoustics
- Aircraft Noise Analysis
- Environmental Noise Assessment
- Acoustic Engineering
- Engineering Education

---

## Future Improvements

- GUI version
- CSV export
- Graphical visualization
- Batch processing
- Unit tests

---

## Author

Gokul Sajeev
Mechanical Engineer | Aerospace Engineering
