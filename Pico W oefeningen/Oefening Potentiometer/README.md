# Oefening Potentiometer

In deze oefening gaan we een variable weerstand/ potentiometer uitlezen. En printen we de ADC(Analog to Digital Converter) in de terminal.

Defenitie ADC:\
``adc_pin = machine.ADC(0)``

Lezen van ADC:\
``adc_value = adc_pin.read_u16()``

Printen van ADC waarde:\
``print("ADC Value:", adc_value)``

