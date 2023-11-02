def solution():
    """Robi Ney wants to fill a 120-liter tub. He is amused by letting the water run for 1 minute, then closing the water supply for 1 minute, and so on alternating opening and closing the water supply. But the cap at the bottom of the tub is not very airtight and lets 1 liter of water escape per minute. The flow rate of the tap is 12 liters per minute. How long does it take to fill the tub in minutes?"""
    # Define the volume of the tub and the flow rate of the tap and the leakage rate
    TUB_VOLUME = 120
    TAP_FLOW_RATE = 12
    LEAKAGE_RATE = 1

    # Initialize the time taken and the volume of water in the tub
    time_taken = 0
    water_volume = 0

    # While the volume of water in the tub is less than the tub volume
    while water_volume < TUB_VOLUME:
        # If the tap is open
        if time_taken % 2 == 0:
            water_volume += TAP_FLOW_RATE # Water flow into tub 

        # If the tap is closed
        else:
            water_volume -= LEAKAGE_RATE # Leakage from tub 

        # Increment the time taken
        time_taken += 1

    # Display the time taken to fill the tub
    result = time_taken
    return result

print(solution())