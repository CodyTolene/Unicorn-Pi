# MIT License
# https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/examples/pico_unicorn/rainbow.py

import time
import uasyncio


async def run(picoUnicorn, graphics):
    width = picoUnicorn.get_width()
    height = picoUnicorn.get_height()

    while True:
        t = time.ticks_ms() / 3600
        for x in range(width):
            for y in range(height):
                # PicoGraphics allows us to set HSV pens directly
                PEN = graphics.create_pen_hsv(t + ((x + y) / width / 4), 1.0, 1.0)
                graphics.set_pen(PEN)
                graphics.pixel(x, y)

        # Ask the Unicorn to update the graphics
        picoUnicorn.update(graphics)

        # And sleep, so we update ~ 60fps
        await uasyncio.sleep(1.0 / 60)


# This section of code is only for testing.
if __name__ == "__main__":
    from picounicorn import PicoUnicorn
    from picographics import PicoGraphics, DISPLAY_UNICORN_PACK

    picoUnicorn = PicoUnicorn()
    graphics = PicoGraphics(display=DISPLAY_UNICORN_PACK)
    uasyncio.run(run(picoUnicorn, graphics))
