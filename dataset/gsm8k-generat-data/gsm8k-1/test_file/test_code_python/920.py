def solution():
    """A three-toed sloth moves very slowly, and only eats when he is up in his tree. For a meal of berries, it takes the sloth 4 hours to make the trip down the tree, pick up berries, and climb back up into his tree. Assuming he picks the same number of berries on each trip, what is the least number of berries he can pick up per trip down to the ground if he wants to collect 24 berries in 8 hours?"""
    hours_per_trip = 4
    total_harvesting_time = 8
    total_berries_wanted = 24
    trips = total_harvesting_time / hours_per_trip
    least_berries_per_trip = total_berries_wanted / trips
    result = least_berries_per_trip
    return result

print(solution())