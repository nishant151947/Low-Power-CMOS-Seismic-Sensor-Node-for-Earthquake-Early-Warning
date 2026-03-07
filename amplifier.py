#------CMOS_amplifier MODEL-------(2)

# amplifier.py
import numpy as np
from scipy.signal import butter, lfilter

def lowpass_filter(data, cutoff, fs, order=1):
    """
    Apply a lowpass Butterworth filter to the signal.
    """
    b, a = butter(order, cutoff/(0.5*fs), btype='low')
    return lfilter(b, a, data)

def amplify(signal, gain=20, bandwidth=10, fs=100, VDD=1.8):
    """
    Amplify signal and limit bandwidth, then clip to CMOS voltage.
    """
    amplified = gain * signal
    filtered = lowpass_filter(amplified, cutoff=bandwidth, fs=fs)
    output = np.clip(filtered, 0, VDD)
    return output