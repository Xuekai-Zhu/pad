def solution():
    """Rory collects rainwater. He has 100 L of rainwater in his tank. During a heavy rainstorm, water flows into the tank at a rate of 2 L/min for 90 minutes. How much water is in the tank at the end of the heavy rain?"""
    # Define the initial amount of water in the tank
    initial_water = 100

    # Define the rate of water flow and the duration of the rainstorm
    flow_rate = 2
    duration = 90

    # Calculate the amount of water added during the rainstorm
    additional_water = flow_rate * duration

    # Calculate the total amount of water in the tank at the end of the rainstorm
    total_water = initial_water + additional_water

    # return the result
    result = total_water
    return result

print(solution())