def solution():
    """James buys 20 pounds of beef and half that much pork. He uses 1.5 pounds of meat to make meals at his restaurant. Each meal sells for $20. How much money did he make?"""
    beef = 20
    pork = beef / 2
    total_meat = beef + pork
    meat_per_meal = 1.5
    meals = total_meat / meat_per_meal
    price_per_meal = 20
    total_income = meals * price_per_meal
    result = total_income
    return result

print(solution())