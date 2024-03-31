# Oefening HC-SR04 afstandsensor

in deze oefening lezen we een ultrasoon sensor uit en berekent hij de afstand voor ons. Deze afstand wordt vervolgens in de Terminal uitgeprint.

Defenitie van de trigger en echo pinnen:\
``trig = Pin(17, Pin.OUT)``\
``echo = Pin(16, Pin.IN, Pin.PULL_DOWN)``

In het volgende stukje wordt de trigger hoog getrokken zodat hij kort een geluid signaal uitzendt. hierna gaat hij een timer starten en als het geluid signaal weer terugkomt op de echo pin dan stop the timer.
```python
     trig.value(0)
     time.sleep(0.1)
     trig.value(1)
     time.sleep_us(2)
     trig.value(0)
     while echo.value()==0:
          pulse_start = time.ticks_us()
     while echo.value()==1:
          pulse_end = time.ticks_us()
```

Berekening afstand:\
``     pulse_duration = pulse_end - pulse_start``\
``     distance = pulse_duration * 17165 / 1000000``

Printen van afstand in terminal:\
``print ('Distance:',"{:.0f}".format(distance),'cm')``
