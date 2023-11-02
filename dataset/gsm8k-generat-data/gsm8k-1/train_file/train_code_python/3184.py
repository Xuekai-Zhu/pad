def solution():
    """Gordon owns 3 restaurants, his first restaurant serves 20 meals,
    his second restaurant serves 40 meals, and his third restaurant serves
    50 meals per day. How many meals do his 3 restaurants serve per week?"""
    meals_per_day_rest1 = 20
    meals_per_day_rest2 = 40
    meals_per_day_rest3 = 50
    days_per_week = 7
    total_meals_per_week = (meals_per_day_rest1 + meals_per_day_rest2 +
                            meals_per_day_rest3) * days_per_week
    result = total_meals_per_week
    return result

print(solution())