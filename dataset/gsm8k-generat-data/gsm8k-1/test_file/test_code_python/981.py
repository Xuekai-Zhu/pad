def solution():
    """Edgar eats 18 pretzels a day. If his brother eats 1/2 as many, how many does his brother eat in a week?"""
    edgar_pretzels_per_day = 18
    brother_pretzels_per_day = edgar_pretzels_per_day / 2
    pretzels_per_week = (edgar_pretzels_per_day + brother_pretzels_per_day) * 7
    result = pretzels_per_week
    return result

print(solution())