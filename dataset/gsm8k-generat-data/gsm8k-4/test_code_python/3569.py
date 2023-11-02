def solution():
    """A tank contains 6000 liters of water, 2000 liters evaporated, and then 3500 liters were drained by Bob. How many liters are in the tank if it now rains for 30 minutes and every 10 minutes 350 liters of rain are added to the tank?"""

    # Define the initial water amount, the amount evaporated and drained
    initial_water = 6000
    evaporated = 2000
    drained = 3500

    # Calculate the amount of water left in the tank
    remaining_water = initial_water - evaporated - drained

    # Calculate the number of times it will rain in 30 minutes
    times_rained = 3

    # Calculate the total amount of water that will be added by rain
    rain_amount = times_rained * 350

    # Calculate the total amount of water in the tank after the rain
    final_amount = remaining_water + rain_amount

    result = final_amount
    return result

print(solution())