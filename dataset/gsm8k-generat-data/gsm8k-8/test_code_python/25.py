def solution():
    starting_balls = 175
    first_100_hit = 2/5 * 100
    remaining_after_first_100 = 100 - first_100_hit
    next_75_hit = 1/3 * 75
    
    total_hit = first_100_hit + next_75_hit
    num_not_hit = starting_balls - total_hit
    result = num_not_hit
    return result

print(solution())