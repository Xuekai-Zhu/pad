def solution():
    """Jacob is trying to eat less than 1800 calories a day. If he eats 400 calories for breakfast, 900 calories for lunch, and 1100 calories for dinner, how many more calories did he eat than he planned?"""
    # Define the maximum number of calories Jacob planned to eat
    max_calories = 1800

    # Calculate the total number of calories Jacob ate
    total_calories = 400 + 900 + 1100

    # Calculate the difference between the actual and planned number of calories
    calories_difference = total_calories - max_calories
    
    # If Jacob ate fewer calories than planned, return 0
    if calories_difference < 0:
        result = 0
    else:
        result = calories_difference
    return result

print(solution())