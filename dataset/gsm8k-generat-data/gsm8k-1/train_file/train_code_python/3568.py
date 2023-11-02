def solution():
    """A tank contains 6000 liters of water, 2000 liters evaporated, and then 3500 liters were drained by Bob. How many liters are in the tank if it now rains for 30 minutes and every 10 minutes 350 liters of rain are added to the tank?"""
    initial_water = 6000
    evaporation = 2000
    drained = 3500
    remaining_water = initial_water - evaporation - drained
    added_rain = 350 * 3
    final_water = remaining_water + added_rain
    result = final_water
    return result

print(solution())