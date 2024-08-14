# Van library "machine" importeren we 1 deel genaamd "Pin". Dit zorgt ervoor dat we alleen het gedeelte importeren wat wij ook effectief gaan gebruiken.
from machine import Pin

# Initialisatie van "led" dat deze een pin van de Pico gaat aansturen. Hierbij geven wij een pin nummer aan en in welke richting de stroom moet gaan.
# "Pin.OUT" voor uitgaande signalen. En "Pin.IN" voor inkomende signalen. Dit is vanuit het perspectief van de Pico.
led = Pin(0, Pin.OUT)

# Hier gebruiken we een functie genaamd "toggle()". Deze functie zet de led van uit naar aan. Of van aan naar uit.
led.toggle()