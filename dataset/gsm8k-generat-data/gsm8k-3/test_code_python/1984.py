def solution():
    """Jacob is trying to eat less than 1800 calories a day. If he eats 400 calories for breakfast, 900 calories for lunch, and 1100 calories for dinner, how many more calories did he eat than he planned?"""
    # Define Jacob's planned daily calorie intake
    planned_calories = 1800

    # Calculate Jacob's total calorie intake for the day
    total_calories = 400 + 900 + 1100

    # Calculate the difference between Jacob's actual calorie intake and his planned intake
    calorie_difference = total_calories - planned_calories

    # Display the calorie difference
    result = calorie_difference
    return result

print(solution())