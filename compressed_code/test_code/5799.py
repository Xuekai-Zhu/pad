def solution():
    
    total_balls = 175
    hit_balls_1 = int(2 / 5 * 100)
    hit_balls_2 = int(1 / 3 * 75)
    total_hit_balls = hit_balls_1 + hit_balls_2
    not_hit_balls = total_balls - total_hit_balls
    result = not_hit_balls
    return result

print(solution())