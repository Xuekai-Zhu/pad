def solution():
    islands = 4
    miles_per_day_island1 = 20
    miles_per_day_island2 = 20
    miles_per_day_island3 = 25
    miles_per_day_island4 = 25
    days_to_explore_each_island = 1.5
    miles_to_walk = (miles_per_day_island1 * days_to_explore_each_island) + (miles_per_day_island2 * days_to_explore_each_island) + (miles_per_day_island3 * days_to_explore_each_island) + (miles_per_day_island4 * days_to_explore_each_island)
    result = miles_to_walk
    return result

print(solution())