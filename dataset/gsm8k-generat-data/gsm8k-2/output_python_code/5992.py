def solution():
    """John wants to lose weight. He eats 1800 calories a day and burns 2300 a day. If he needs to burn 4000 calories to lose 1 pound how many days will it take to lose 10 pounds?"""
    calories_to_lose_one_pound = 4000
    pounds_to_lose = 10
    total_calories_to_lose = calories_to_lose_one_pound * pounds_to_lose
    daily_calorie_deficit = 500  # difference between calories consumed and calories burned
    days_to_lose_weight = total_calories_to_lose / (daily_calorie_deficit)
    result = days_to_lose_weight
    return result

print(solution())