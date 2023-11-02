def solution():
    """Jacob is trying to eat less than 1800 calories a day. If he eats 400 calories for breakfast, 900 calories for lunch, and 1100 calories for dinner, how many more calories did he eat than he planned?"""
    planned_calories = 1800
    breakfast_calories = 400
    lunch_calories = 900
    dinner_calories = 1100
    total_calories = breakfast_calories + lunch_calories + dinner_calories
    excess_calories = total_calories - planned_calories
    result = excess_calories
    return result

print(solution())