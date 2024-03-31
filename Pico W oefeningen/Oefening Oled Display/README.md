# Oefening Oled Display

In deze oefening gaan we een oled display aansturen over I2C protocol. Voor deze oefening is een custom library nodig die we zelf moeten importeren. 

er zijn 2 files voor deze oefening\
[main.py](https://github.com/RunningZeus5334/RPI_Pico_oefeningen/blob/RunningZeus5334-patch-1/Pico%20W%20oefeningen/Oefening%20Oled%20Display/main.py)\
[sh1106](https://github.com/RunningZeus5334/RPI_Pico_oefeningen/blob/RunningZeus5334-patch-1/Pico%20W%20oefeningen/Oefening%20Oled%20Display/sh1106.py)

De sh1106 file is de library. Deze moet je op de Pico's interne opslag zetten.

### Uitleg Code:
Defenitie van hoogte en breedte scherm:\
``WIDTH  = 128``\
``HEIGHT = 64``

Initalisatie van oled display:\
``oled = SH1106_I2C(WIDTH, HEIGHT, i2c)`` 

het laden van de raspberry foto:
```python
buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)
```
Leegmaken van het display:\
``oled.fill(0)``

De foto plaatsen op het scherm:\
``oled.blit(fb, 96, 0)``

Tekst plaatsen op het scherm:\
``oled.text("Raspberry Pi",5,5)``\
``oled.text("Pico",5,15)``

Het effectief schrijven naar het scherm:\
``oled.show()``


### Handige links:

Links naar de libs:\
[Library + Code](https://github.com/raspberrypi/pico-micropython-examples/blob/master/i2c/1106oled/README.adoc)\
[Library uitleg](https://github.com/robert-hh/SH1106)
