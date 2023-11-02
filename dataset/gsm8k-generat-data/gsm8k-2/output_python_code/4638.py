def solution():
    """John scores 2 shots worth 2 points and 1 shot worth 3 points every 4 minutes. He plays for 2 periods. Each period is 12 minutes. How many points does he score?"""
    points = 0
    period_time = 12
    for i in range(2):
        for j in range(3):
            points += 2
        points += 3
        for k in range(3):
            points += 2
        points += 3
        for l in range(3):
            points += 2
        points += 3
    result = points
    return result

print(solution())