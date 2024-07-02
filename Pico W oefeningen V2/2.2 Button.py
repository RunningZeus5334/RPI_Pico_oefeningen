import machine
import time

# We initializeren de knop. Verander hier '1' voor de juiste pin.
# We gebruiken machine.Pin.IN omdat we nu een signaal 'in' willen hebben om de knop uit te lezen.
# We gebruiken machine.Pin.PULL_DOWN om te verzekeren dat de pico niet een ingeduwde pin meet wanneer die niet ingeduwd is.
# Voor meer informatie hierover vraag een begeleider.
button_pin = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    # We lezen de waarde van de ingestelde pin en bewaren deze in de variabele 'button_state'.
    button_state = button_pin.value()
    
    # We printen de uitgelezen staat van de knop naar de console.
    print("Button State:", button_state)
    
    # We wachten kort om een vertraging te creëren tussen de loops.
    time.sleep(0.1)
    
# Je weet nu hoe 'if' werkt en hoe je knoppen en leds gebruikt in python.
# Verander de code nu zodat je met een druk op een knop een led lamp aan of uit zet.
# Tip: kopieer code van vorige opdrachten.

# Extra uitdaging: verbind 3 knoppen en laat elke appart een led kleur aansturen.