def solution():
    """Jonathan eats 2500 calories every day except for Saturday, when he consumes an extra 1000 calories. He burns 3000 calories every day. What is his weekly caloric deficit?"""
    calories_eaten_per_day = 2500
    extra_calories_on_Saturday = 1000
    calories_burned_per_day = 3000
    total_calories_eaten_per_week = (calories_eaten_per_day * 6) + (calories_eaten_per_day + extra_calories_on_Saturday)
    total_calories_burned_per_week = calories_burned_per_day * 7
    caloric_deficit_per_week = total_calories_burned_per_week - total_calories_eaten_per_week
    result = caloric_deficit_per_week
    return result

print(solution())