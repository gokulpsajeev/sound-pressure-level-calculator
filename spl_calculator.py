import math

print("====================================")
print(" SOUND PRESSURE LEVEL CALCULATOR")
print("====================================")

pressure = float(input("Enter RMS Sound Pressure (Pa): "))

REFERENCE_PRESSURE = 20e-6

spl = 20 * math.log10(pressure / REFERENCE_PRESSURE)

print("\nResults")
print("-----------------------------")
print(f"Input Pressure : {pressure:.6f} Pa")
print(f"SPL            : {spl:.2f} dB")