def solution():
    """Jerry has a flock of chickens. The red chickens produce 3 eggs a day, and the white chickens produce 5 eggs a day. Every day Jerry collects 42 eggs. If he has two more white chickens than red chickens, how many red chickens does he have?"""
    total_eggs = 42
    red_eggs_per_day = 3
    white_eggs_per_day = 5
    white_chickens = (total_eggs - red_eggs_per_day * x) / (white_eggs_per_day - red_eggs_per_day)
    red_chickens = white_chickens - 2
    result = red_chickens
    return result

print(solution())