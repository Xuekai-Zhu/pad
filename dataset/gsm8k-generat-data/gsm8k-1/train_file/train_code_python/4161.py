def solution():
    """Jerry's breakfast includes 6 pancakes with 120 calories each, two strips of bacon with 100 calories each, and a bowl of cereal with 200 calories. How many calories is his breakfast total?"""
    pancake_calories = 120
    bacon_calories = 100
    cereal_calories = 200
    total_pancake_calories = 6 * pancake_calories
    total_bacon_calories = 2 * bacon_calories
    total_calories = total_pancake_calories + total_bacon_calories + cereal_calories
    result = total_calories
    return result

print(solution())