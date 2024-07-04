# Cody Tolene
# Apache License 2.0

import uasyncio
from utils.view_manager import switch_view


# Button listener process
async def buttonListenerProcess(
    views, picoUnicorn, graphics, currentViewKey, currentViewTask
):
    buttonAState = False
    buttonXState = False

    view_keys = list(views.keys())

    while True:
        # Check if button A is pressed
        if picoUnicorn.is_pressed(picoUnicorn.BUTTON_A):
            if not buttonAState:
                buttonAState = True
                current_index = view_keys.index(currentViewKey)
                currentViewKey = view_keys[(current_index - 1) % len(view_keys)]
                currentViewTask = await switch_view(
                    views, currentViewKey, currentViewTask, picoUnicorn, graphics
                )
        else:
            buttonAState = False

        # Check if button X is pressed
        if picoUnicorn.is_pressed(picoUnicorn.BUTTON_X):
            if not buttonXState:
                buttonXState = True
                current_index = view_keys.index(currentViewKey)
                currentViewKey = view_keys[(current_index + 1) % len(view_keys)]
                currentViewTask = await switch_view(
                    views, currentViewKey, currentViewTask, picoUnicorn, graphics
                )
        else:
            buttonXState = False

        # Handle B and Y button presses in the views themselves

        # Sleep for a short period to debounce button presses
        await uasyncio.sleep(0.1)
