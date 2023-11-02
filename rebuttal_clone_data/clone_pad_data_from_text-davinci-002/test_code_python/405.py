def solution():
    river_width = 42
    boat_width = 3
    space_between = 2
    max_boats = (river_width - boat_width) / (boat_width + space_between)
    result = max_boats
    return result

print(solution())