def solution():
    original_rocks = 10
    eaten_rocks = original_rocks / 2
    spit_out_rocks = 2
    remaining_rocks = original_rocks - eaten_rocks + spit_out_rocks
    result = remaining_rocks
    return result

print(solution())