#-------STA/LTA Detection---------(4)
import numpy as np

def sta_lta(signal, fs, sta_sec=0.5, lta_sec=5, threshold=3):
    """
    Short-Term Average / Long-Term Average earthquake detection.
    """
    sta_samples = int(sta_sec * fs)
    lta_samples = int(lta_sec * fs)
    
    sta = np.convolve(np.abs(signal), np.ones(sta_samples)/sta_samples, mode='same')
    lta = np.convolve(np.abs(signal), np.ones(lta_samples)/lta_samples, mode='same')
    
    ratio = sta / (lta + 1e-6)  # avoid division by zero
    detection = ratio > threshold
    return ratio, detection  