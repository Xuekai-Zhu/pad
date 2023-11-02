def solution():
    """Andrea buys herself a pony for her 30th birthday. She pays $500/month to rent a pasture for it, $10 a day for food, and $60/lesson for two lessons a week. How much does she spend on her pony in a year?"""
    pasture_cost = 500 * 12
    food_cost = 10 * 365
    lesson_cost = 60 * 2 * 52
    total_cost = pasture_cost + food_cost + lesson_cost
    result = total_cost
    return result

print(solution())