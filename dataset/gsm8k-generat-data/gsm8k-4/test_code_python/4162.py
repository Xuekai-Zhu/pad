def solution():
    """Jerry's breakfast includes 6 pancakes with 120 calories each, two strips of bacon with 100 calories each, and a bowl of cereal with 200 calories. How many calories is his breakfast total?"""
    # Define the number of pancakes and the calorie count per pancake
    pancakes_count = 6
    pancakes_calories = 120

    # Define the number of bacon strips and the calorie count per strip
    bacon_count = 2
    bacon_calories = 100

    # Define the calorie count for the bowl of cereal
    cereal_calories = 200

    # Calculate the total calorie count for the breakfast
    total_calories = (pancakes_count * pancakes_calories) + (bacon_count * bacon_calories) + cereal_calories

    # Return the result
    result = total_calories
    return result

print(solution())