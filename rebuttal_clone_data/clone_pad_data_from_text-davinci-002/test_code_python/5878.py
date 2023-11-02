def solution():
    pebble_width = 1/4
    rock_width = 1/2
    boulder_width = 2
    number_of_pebbles = 6
    number_of_rocks = 3
    number_of_boulders = 2
    total_width = (pebble_width * number_of_pebbles) + (rock_width * number_of_rocks) + (boulder_width * number_of_boulders)
    result = total_width
    return result

print(solution())