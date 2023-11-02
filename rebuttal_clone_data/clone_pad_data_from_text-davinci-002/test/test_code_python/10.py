def solution():
    
    total_balls = 175
    balls_hit = ((2 / 5) * 100) + ((1 / 3) * 75)
    balls_missed = total_balls - balls_hit
    result = balls_missed
    return result

print(solution())