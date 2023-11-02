def solution():
    """A tank contains 6000 liters of water, 2000 liters evaporated, and then 3500 liters were drained by Bob. How many liters are in the tank if it now rains for 30 minutes and every 10 minutes 350 liters of rain are added to the tank?"""
    initial_water = 6000
    evaporated_water = 2000
    drained_water = 3500
    remaining_water = initial_water - evaporated_water - drained_water

    for i in range(3):
        remaining_water += 350
        # add 350 liters of rain every 10 minutes

    result = remaining_water
    return result

print(solution())