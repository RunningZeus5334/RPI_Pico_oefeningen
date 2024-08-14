# De volgende code is geschreven door Chat GPT.
# We verwachten niet dat je dit begrijpt, maar het is wel heel leuk om het resultaat te zien.
# Pas was variabelen aan om het te laten werken, en om te zien wat het doet.

from picozero import RGBLED
import time

rgb = RGBLED(red=1, green=2, blue=3)

def fade_color(target_color, duration=1, steps=100):
    current_color = list(rgb.color)
    step_delay = duration / steps

    delta_color = [(target_color[i] - current_color[i]) / steps for i in range(3)]

    for _ in range(steps):
        current_color = [current_color[i] + delta_color[i] for i in range(3)]
        rgb.color = tuple(map(int, current_color))
        time.sleep(step_delay)

while True:
    # Fade to red
    fade_color((255, 0, 0))
    time.sleep(0.5)

    # Fade to green
    fade_color((0, 255, 0))
    time.sleep(0.5)

    # Fade to blue
    fade_color((0, 0, 255))
    time.sleep(0.5)

    # Fade to yellow
    fade_color((255, 255, 0))
    time.sleep(0.5)

    # Fade to purple
    fade_color((255, 0, 255))
    time.sleep(0.5)

    # Fade to cyan
    fade_color((0, 255, 255))
    time.sleep(0.5)

    # Fade to white
    fade_color((255, 255, 255))
    time.sleep(0.5)