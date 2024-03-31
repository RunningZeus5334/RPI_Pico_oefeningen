# Oefening Infra Rood Sensor

In deze oefening lezen we een infra rood sensor in en printen we de status in de Terminal.

Definitie van de sensor:\
``sensor_pin = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)``

Uitlezen van de sensor:\
Deze sensor is normally closed. dus we zetten not het uitlezen zodat de waarde geinverteerd wordt.\
``sensor_state = not sensor_pin.value()``

Printen van status:\
``print("Sensor State:", sensor_state)``
