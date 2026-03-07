#---------main.py-----------------------

import matplotlib.pyplot as plt
from signal import generate_seismic_signal
from amplifier import amplify
from adc import adc_quantize
from detection import sta_lta
from power_analysis import estimate_power

#--------sampling frequency generate------
fs = 100 
#------------- Generate Signal-----------

t, sensor_signal = generate_seismic_signal(fs=fs)


#----------------- Amplify --------------

amplified_signal = amplify(sensor_signal, fs=fs)


#------------------- ADC ----------------

digital_signal = adc_quantize(amplified_signal)


#----------------- Detection -------------

ratio, detection = sta_lta(digital_signal, fs)


#------------------- Power-----------------

power = estimate_power()
print("Estimated Power:", power, "Watts")


#----------------Plot Results---------------

plt.figure(figsize=(12,10))

plt.subplot(4,1,1)
plt.plot(t, sensor_signal)
plt.title("Raw Seismic Signal")

plt.subplot(4,1,2)
plt.plot(t, amplified_signal)
plt.title("Amplified Signal")

plt.subplot(4,1,3)
plt.plot(t, ratio)
plt.title("STA/LTA Ratio")

plt.subplot(4,1,4)
plt.plot(t, detection.astype(int))
plt.title("Detection Output")

plt.tight_layout()
plt.show()