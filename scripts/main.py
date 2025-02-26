# Apache License Version 2.0
# Cody Tolene

import uasyncio
import sys

from collections import OrderedDict
from picographics import PicoGraphics, DISPLAY_UNICORN_PACK
from picounicorn import PicoUnicorn

from views import digital_clock_view
from views import digital_rain_view
from views import dvd_bouncer_view
from views import emergency_view
from views import fire_view
from views import fireflies_view
from views import fireplace_view
from views import fireworks_view
from views import flashlight_torch_view
from views import lava_lamp_view
from views import lightning_view
from views import plasma_view
from views import rainbow_view
from views import raindrops_view
from views import snowfall_view
from views import sos_view
from views import warp_speed_view
from views import wave_view

from utils.button_listener import buttonListenerProcess
from utils.view_manager import load_current_view_index

# Ensure local packages can be imported
sys.path.append("/utils")
sys.path.append("/views")

# Initialize PicoUnicorn & PicoGraphics
picoUnicorn = PicoUnicorn()
graphics = PicoGraphics(display=DISPLAY_UNICORN_PACK)

# Ordered dictionary of view functions
views = OrderedDict(
    [
        ("Digital Clock", digital_clock_view.run),
        ("Digital Rain", digital_rain_view.run),
        ("DVD Bouncer", dvd_bouncer_view.run),
        ("Emergency", emergency_view.run),
        ("Fire", fire_view.run),
        ("Fireflies", fireflies_view.run),
        ("Fireplace", fireplace_view.run),
        ("Fireworks", fireworks_view.run),
        ("Flashlight Torch", flashlight_torch_view.run),
        ("Lava Lamp", lava_lamp_view.run),
        ("Lightning", lightning_view.run),
        ("Plasma", plasma_view.run),
        ("Rainbow", rainbow_view.run),
        ("Raindrops", raindrops_view.run),
        ("SOS", sos_view.run),
        ("Snowfall", snowfall_view.run),
        ("Warp Speed", warp_speed_view.run),
        ("Wave", wave_view.run),
    ]
)

# Current key of the view being displayed
currentViewKey = load_current_view_index()

# Task to keep track of the current running view
currentViewTask = None

if __name__ == "__main__":
    # Clear the screen initially
    graphics.set_pen(0)  # Black
    graphics.clear()
    picoUnicorn.update(graphics)

    # Start the asyncio event loop
    loop = uasyncio.get_event_loop()

    # Start the initial view
    currentViewTask = loop.create_task(views[currentViewKey](picoUnicorn, graphics))

    # Create and schedule the button listener coroutine
    loop.create_task(
        buttonListenerProcess(
            views, picoUnicorn, graphics, currentViewKey, currentViewTask
        )
    )

    # Run the event loop forever
    loop.run_forever()
