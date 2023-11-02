def solution():
    """Jonathan eats 2500 calories every day except for Saturday, when he consumes an extra 1000 calories. He burns 3000 calories every day. What is his weekly caloric deficit?"""
    daily_calories = 2500
    saturday_calories = 3500
    daily_burned_calories = 3000
    weekly_deficit = (6 * daily_calories + saturday_calories - 7 * daily_burned_calories)
    result = weekly_deficit
    return result

print(solution())