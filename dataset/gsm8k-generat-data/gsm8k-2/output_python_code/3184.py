def solution():
    """Gordon owns 3 restaurants, his first restaurant serves 20 meals, his second restaurant serves 40 meals, and his third restaurant serves 50 meals per day. How many meals do his 3 restaurants serve per week?"""
    meals_per_day = [20, 40, 50]
    days_per_week = 7
    total_meals_per_week = sum(meals_per_day) * days_per_week
    result = total_meals_per_week
    return result

print(solution())