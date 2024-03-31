# Oefening Button

in deze code wordt er een knop ingelezen. En wordt er in de terminal geprint wat de status is van de knop.

Defenitie van de input:
``button_pin = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)`` 

Het uitlezen van de knop:
``button_state = button_pin.value()``

Printen in terminal van de knop status:
``print("Button State:", button_state)``
