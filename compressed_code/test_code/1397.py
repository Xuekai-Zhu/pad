def solution():
    
    starting_rocks = 10
    eaten_rocks = starting_rocks / 2
    spit_out_rocks = 2
    remaining_rocks = starting_rocks - eaten_rocks + spit_out_rocks
    result = remaining_rocks
    return result

print(solution())