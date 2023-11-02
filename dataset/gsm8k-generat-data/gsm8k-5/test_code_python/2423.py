def solution():
    initial_water = 100  # Rory has 100 L of rainwater in his tank
    flow_rate = 2  # Water flows into the tank at a rate of 2 L/min
    time = 90  # The heavy rainstorm lasts for 90 minutes

    # Calculate the additional water collected during the heavy rainstorm
    additional_water = flow_rate * time

    # Calculate the total water in the tank after the heavy rainstorm
    total_water = initial_water + additional_water
    result = total_water
    return result

print(solution())