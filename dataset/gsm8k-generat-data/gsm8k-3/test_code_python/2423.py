def solution():
    """Rory collects rainwater. He has 100 L of rainwater in his tank. During a heavy rainstorm, water flows into the tank at a rate of 2 L/min for 90 minutes. How much water is in the tank at the end of the heavy rain?"""
    # Define the initial amount of rainwater in the tank
    initial_water = 100

    # Calculate the amount of water that flows into the tank during the heavy rain
    flow_rate = 2 # liters per minute
    time = 90 # minutes
    added_water = flow_rate * time

    # Calculate the total amount of water in the tank after the heavy rain
    total_water = initial_water + added_water

    # Display the total amount of water in the tank
    result = total_water
    return result

print(solution())