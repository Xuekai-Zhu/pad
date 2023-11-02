def solution():
    """Robi Ney wants to fill a 120-liter tub. He is amused by letting the water run for 1 minute, then closing the water supply for 1 minute, and so on alternating opening and closing the water supply. But the cap at the bottom of the tub is not very airtight and lets 1 liter of water escape per minute. The flow rate of the tap is 12 liters per minute. How long does it take to fill the tub in minutes?"""
    # Define the volume of the tub and the escape rate
    TUB_VOLUME = 120
    ESCAPE_RATE = 1

    # Define the flow rate of the tap and the time-spent values
    FLOW_RATE = 12
    time_spent_open = 1
    time_spent_close = 1

    # Initialize the water level and the timer
    water_level = 0
    timer = 0

    # While the tub is not full, alternate opening and closing the tap
    while water_level < TUB_VOLUME:
        # Open the tap for a minute
        water_level += FLOW_RATE * time_spent_open
        
        # Close the tap for a minute
        water_level -= ESCAPE_RATE * time_spent_close
        
        # Increment the timer
        timer += (time_spent_open + time_spent_close)

    # Return the timer
    result = timer
    return result

print(solution())