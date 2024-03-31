from machine import Pin
from machine import PWM
from time import sleep

pwm = PWM(Pin(6))
pwm.freq(50)

# Servo functie
def setServoCycle (position):
    pwm.duty_u16(position)
    sleep(0.01)

while True:
    for pos in range(1000,9000,50):
        setServoCycle(pos)
    for pos in range(9000,1000,-50):
        setServoCycle(pos)