#---generate the seismic signal -----(1)
import numpy as np

def generate_seismic_signal(fs=100, duration=15):
    """
    Generate a synthetic seismic signal with noise, P-wave, and S-wave.
    
    Args:
        fs: Sampling frequency (samples/sec)
        duration: Total time of the signal in seconds
        
    Returns:
        t: Time array
        signal: Seismic signal array
    """
    t = np.arange(0, duration, 1/fs)
    
    noise = 0.02 * np.random.randn(len(t))                 # Noise
    P = 0.08 * np.sin(2*np.pi*8*t) * ((t > 3) & (t < 5))   # P-wave
    S = 0.5 * np.sin(2*np.pi*3*t) * ((t > 7) & (t < 12))   # S-wave
    
    signal = noise + P + S
    return t, signal