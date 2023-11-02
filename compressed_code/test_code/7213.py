def solution():
    
    initial_rocks = 10
    rocks_eaten = initial_rocks / 2
    rocks_spit_out = 2
    rocks_left = initial_rocks - rocks_eaten + rocks_spit_out
    result = rocks_left
    return result

print(solution())