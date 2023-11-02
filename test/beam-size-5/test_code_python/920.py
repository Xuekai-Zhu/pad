def solution():
    
    # Define the number of berries the sloth takes for the meal of berries
    sloth_time = 4

    # Calculate the number of berries the sloth can collect in 8 hours
    total_time = 8

    # Calculate the number of berries the sloth can pick up per trip
    berries_per_trip = (total_time / sloth_time) / 24

    # Calculate the minimum number of berries the sloth can pick up per trip down to the ground
    min_berries_per_trip = berries_per_trip - berries_per_trip

    # Display the minimum number of berries the sloth can pick up per trip down
    result = min_berries_per_trip
    return result

print(solution())