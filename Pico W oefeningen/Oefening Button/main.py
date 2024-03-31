import machine
import time

# Define the pin connected to the button
button_pin = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    # Read the state of the button
    button_state = button_pin.value()
    
    # Print the state of the button
    print("Button State:", button_state)
    
    # Wait for a short delay
    time.sleep(0.1)
