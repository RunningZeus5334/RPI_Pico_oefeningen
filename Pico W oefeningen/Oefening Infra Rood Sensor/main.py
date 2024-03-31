import machine
import time

# Define the pin connected to the button
sensor_pin = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    # Read the state of the button
    sensor_state = not sensor_pin.value()
    
    # Print the state of the button
    print("Sensor State:", sensor_state)
    
    # Wait for a short delay
    time.sleep(0.1)
