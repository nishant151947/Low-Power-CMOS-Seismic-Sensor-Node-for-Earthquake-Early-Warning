#-----analog to digital converter (QUANTISATION)------(3)
import numpy as np

def adc_quantize(signal, Vref=1.8, bits=10):
    """
    Convert analog signal to digital using ADC quantization.
    """
    levels = 2**bits
    quantized = np.round((signal/Vref)*(levels-1))
    digital_output = quantized*(Vref/(levels-1))
    return digital_output