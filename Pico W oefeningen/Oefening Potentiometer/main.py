import machine
import time

# Define the ADC pin
adc_pin = machine.ADC(0)

while True:
    # Read the ADC value
    adc_value = adc_pin.read_u16()
    
    # Print the ADC value to the terminal
    print("ADC Value:", adc_value)
    
    # Wait for a short delay
    time.sleep(0.1)
