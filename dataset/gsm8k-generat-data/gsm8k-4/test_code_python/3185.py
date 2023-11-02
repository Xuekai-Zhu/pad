def solution():
    """Gordon owns 3 restaurants, his first restaurant serves 20 meals,
    his second restaurant serves 40 meals, and his third restaurant serves 50 meals per day.
    How many meals do his 3 restaurants serve per week?"""
    # Calculate the total number of meals served per day
    total_meals_per_day = 20 + 40 + 50

    # Calculate the total number of meals served per week
    total_meals_per_week = total_meals_per_day * 7

    # return the result
    result = total_meals_per_week
    return result

print(solution())