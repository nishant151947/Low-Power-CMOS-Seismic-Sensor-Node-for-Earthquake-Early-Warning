#------CMOS Power Analysis--------(5)

def estimate_power(C_load=10e-12, VDD=1.8, freq=10):
    """
    Estimate dynamic power of a CMOS circuit.
    """
    power = C_load * (VDD**2) * freq
    return power