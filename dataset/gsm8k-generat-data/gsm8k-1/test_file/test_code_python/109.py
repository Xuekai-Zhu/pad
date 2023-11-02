def solution():
    """Ryan plants 2 flowers a day in his garden. After 15 days, how many flowers does he have if 5 did not grow?"""
    flowers_planted_per_day = 2
    days_planted = 15
    flowers_not_grown = 5
    total_flowers = (flowers_planted_per_day * days_planted) - flowers_not_grown
    result = total_flowers
    return result

print(solution())