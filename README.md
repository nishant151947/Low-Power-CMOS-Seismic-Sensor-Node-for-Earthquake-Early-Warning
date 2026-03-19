# Seismic Signal Detection System Simulation

A Python-based simulation of a **seismic sensing node** that models the full signal processing pipeline used in earthquake monitoring systems. The project simulates signal acquisition, analog amplification, analog-to-digital conversion, and seismic event detection using the **STA/LTA algorithm**.

# Overview

Seismic monitoring systems detect ground vibrations caused by earthquakes or other geological events. These systems consist of multiple stages that convert weak analog signals from sensors into meaningful digital information.

This project recreates the essential components of such a system in software, allowing users to understand how seismic signals are processed from raw sensor data to event detection.

The simulation models:

* Synthetic seismic signal generation
* CMOS amplifier behavior
* Analog filtering
* ADC quantization
* STA/LTA event detection

# System Architecture

The signal processing pipeline used in this project follows the structure of real seismic monitoring devices:

```
Synthetic Seismic Signal
        ↓
CMOS Amplifier Model
        ↓
Low-pass Filtering
        ↓
ADC Quantization
        ↓
STA/LTA Event Detection
        ↓
Seismic Event Detection Output
```

Each stage represents a key component of a real-world seismic sensing system.

# Key Components

## 1. Synthetic Seismic Signal Generation

The system begins by generating a synthetic signal that mimics seismic activity. The signal contains:

* background noise
* vibration patterns representing seismic waves

This simulated signal acts as the output of a seismic sensor such as a **geophone or accelerometer**.

## 2. CMOS Amplifier Simulation

Real seismic sensors produce extremely weak electrical signals. These signals must be amplified before processing.

The amplifier module performs three functions:

### Signal Amplification

The input signal is multiplied by a gain factor to increase its amplitude.

### Bandwidth Limitation

A Butterworth low-pass filter is applied to remove high-frequency noise and simulate the limited bandwidth of real amplifiers.

### Voltage Saturation

The signal is clipped between **0 V and 1.8 V**, simulating the voltage limits of CMOS circuits.

## 3. Analog-to-Digital Conversion (ADC)

Before digital processing, analog signals must be converted into discrete digital values.

This project simulates a **10-bit ADC** using quantization.

For a 10-bit converter:

```
Number of quantization levels = 2^10 = 1024
```

The analog signal is mapped to the nearest digital level within the reference voltage range.

## 4. STA/LTA Event Detection

To detect seismic events, the project implements the **Short-Term Average / Long-Term Average (STA/LTA) algorithm**, a standard method used in earthquake monitoring.

### Short-Term Average (STA)

Represents the signal energy within a short time window and reacts quickly to sudden changes.

### Long-Term Average (LTA)

Represents the background noise level using a much longer time window.

### Detection Rule

```
STA / LTA > Threshold
```

When this condition is satisfied, the system identifies a potential seismic event.

## Signal Processing Pipeline Visualization

The following figure shows the complete seismic signal processing pipeline, including raw signal generation, amplification, STA/LTA ratio computation, and final detection output.

<p align="center">
  <img src="seismic_pipeline.png" width="800">
</p>

# Technologies Used

* Python
* NumPy
* SciPy
* Digital Signal Processing concepts

# Applications

This simulation framework demonstrates techniques used in:

* Earthquake monitoring systems
* Structural vibration monitoring
* Embedded sensing systems
* IoT-based environmental monitoring
* Low-power sensor networks

# Learning Outcomes

This project demonstrates:

* Signal processing fundamentals
* Analog front-end modeling
* ADC quantization concepts
* Event detection algorithms
* Scientific computing using Python

---

# Conclusion

This project demonstrates how a complete seismic sensing pipeline can be simulated using Python. By modeling amplification, filtering, digitization, and event detection, the system provides a clear understanding of how real seismic monitoring devices operate.



