def solution():
    # Distance traveled eastward on the first day
    distance_traveled_east = 30 * 20

    # Distance from the starting point to the midpoint of the journey
    distance_to_midpoint = 2 * distance_traveled_east

    # Distance traveled westward during the storm
    distance_traveled_west = distance_to_midpoint - (distance_to_midpoint / 3)

    result = distance_traveled_west
    return result

print(solution())