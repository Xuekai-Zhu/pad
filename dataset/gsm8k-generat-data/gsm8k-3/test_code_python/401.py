def solution():
    """Sam works at the Widget Factory, assembling Widgets. He can assemble 1 widget every 10 minutes. Jack from the loading dock can help assemble widgets when he doesn't have anything else to do. When he helps, they put together 2 complete widgets every 15 minutes. Recently the factory hired Tony to help assemble widgets. Being new to the job, he doesn't work as fast as Sam or Jack. Yesterday Sam worked for 6 hours before he had to leave work early for a dentist appointment. Jack was able to help out for 4 hours before he had to go back to the loading dock to unload a new shipment of widget materials. Tony worked the entire 8-hour shift. At the end of the day, they had completed 68 widgets. How long does it take Tony to assemble a Widget, in minutes?"""
    # Define the widget assembly rates for Sam, Jack, and Tony
    SAM_RATE = 1/10
    JACK_RATE = 2/15
    TONY_RATE = 1/x

    # Define the working time for Sam, Jack, and Tony
    SAM_TIME = 6 * 60
    JACK_TIME = 4 * 60
    TONY_TIME = 8 * 60

    # Calculate the number of widgets assembled by Sam and Jack
    sam_widgets = SAM_RATE * SAM_TIME
    jack_widgets = JACK_RATE * JACK_TIME

    # Calculate the number of widgets assembled by Tony
    total_widgets = 68
    tony_widgets = total_widgets - sam_widgets - jack_widgets

    # Calculate the time it takes Tony to assemble 1 widget
    tony_rate = tony_widgets / TONY_TIME
    x = 1 / tony_rate

    # Display the time it takes Tony to assemble 1 widget, in minutes
    result = x
    return result

print(solution())