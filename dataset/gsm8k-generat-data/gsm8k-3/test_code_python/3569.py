def solution():
    """A tank contains 6000 liters of water, 2000 liters evaporated, and then 3500 liters were drained by Bob. How many liters are in the tank if it now rains for 30 minutes and every 10 minutes 350 liters of rain are added to the tank?"""
    # Define the initial amount of water in the tank
    initial_water = 6000

    # Calculate the amount of water remaining after evaporation and drainage
    remaining_water = initial_water - 2000 - 3500

    # Calculate the amount of rain added to the tank in 30 minutes
    rain_added = 350 * 3

    # Calculate the total amount of water in the tank after the rain
    total_water = remaining_water + rain_added

    # Display the total amount of water in the tank
    result = total_water
    return result

print(solution())