# Soms is het handig om beschikking te hebben tot extra functies die niet standaard geladen worden in pyton.
# Hiervoor importeren we 'libraries'. 
# We importeren nu de library 'time' om te kunnen wachten tussen verschillende lijnen code.

from time import sleep

print("We wachten nu 1 seconde.")

sleep(1)

print("1 seconde is voorbij gegaan.")

# De sleep() functie laat de code een aantal secondes wachten dat tusseen de haakjes staat.
# We typen time. voor sleep om aan te geven dat sleep te vinden is in de geimporteerde library time.

# Soms willen we alleen specifieke functies van een library gebruiken.
# Dan is het handig om deze functie los te importeren.
# Vervang 'import time' met 'from time import sleep', en 'time.sleep(1)' met 'sleep(1)'.
# De code zou nu precies hetzelfde moeten doen.