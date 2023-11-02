def solution():
    
    # Define the initial amount of water in the pool
    initial_water = 10000

    # Calculate the amount of water used to fill the tank
    water_used = initial_water / 2

    # Calculate the amount of water remaining in the tank after 6 days
    remaining_water = initial_water - water_used - 500 * 6

    # Display the amount of water remaining in the tank
    result = remaining_water
    return result

print(solution())