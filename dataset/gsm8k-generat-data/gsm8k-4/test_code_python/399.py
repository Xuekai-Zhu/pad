def solution():
    """Sam works at the Widget Factory, assembling Widgets. He can assemble 1 widget every 10 minutes. Jack from the loading dock can help assemble widgets when he doesn't have anything else to do. When he helps, they put together 2 complete widgets every 15 minutes. Recently the factory hired Tony to help assemble widgets. Being new to the job, he doesn't work as fast as Sam or Jack. Yesterday Sam worked for 6 hours before he had to leave work early for a dentist appointment. Jack was able to help out for 4 hours before he had to go back to the loading dock to unload a new shipment of widget materials. Tony worked the entire 8-hour shift. At the end of the day, they had completed 68 widgets. How long does it take Tony to assemble a Widget, in minutes?"""
    # Define the assembly rates of Sam, Jack and Tony in widgets per minute
    sam_rate = 1 / 10
    jack_rate = 2 / 15
    tony_rate = (68 - (6 * 60 * sam_rate + 4 * 60 * jack_rate)) / (8 * 60)

    # Calculate the time it takes Tony to assemble a widget in minutes
    tony_time = 1 / tony_rate

    # Return the result
    result = tony_time
    return result

print(solution())