# Probeer de led langzamer te laten knipperen. 
from machine import Pin
import time

led = Pin(0, Pin.OUT)

# Dit is een 'while loop'.
# Dit betekend dat de code hieronder uitgevoerd blijft worden zolang wat na 'while' staat waar is.
# Omdat wat na 'while' staat 'True' is, en 'True' altijd waar is, zal de loop oneindig door blijven gaan.
while True:
    
    # In een loop moeten we voor een lijn code een tab toevoegen. Dit geeft aan dat die lijn code in de loop moet uitgevoerd worden. 
    # "time.sleep" wordt hier toegevoegd om een vertraging te zetten tussen de "led.toggle". Dit zorgt ervoor dat de led niet te snel gaat knipperen. 
    time.sleep(0.1)
    led.toggle()

