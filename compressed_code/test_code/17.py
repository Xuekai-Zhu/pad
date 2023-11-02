def solution():
    
    total_balls = 175
    first_100_hit = int(2/5 * 100)
    next_75_hit = int(1/3 * 75)
    total_hit = first_100_hit + next_75_hit
    not_hit = total_balls - total_hit
    result = not_hit
    return result

print(solution())