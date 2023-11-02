def solution():
    
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