def solution():
    """Voldemort had his dinner and ate a piece of cake that has 110 calories. He also ate 1 pack of chips that contained 310 calories and drank a 500 ml bottle of coke that has 215 calories. His caloric intake for breakfast and lunch is 560 and 780 calories, respectively. If he has a 2500 calorie intake limit per day, how many calories can he still take?"""
    dinner_calories = 110 + 310 + 215
    breakfast_calories = 560
    lunch_calories = 780
    total_calories_consumed = dinner_calories + breakfast_calories + lunch_calories
    calorie_limit = 2500
    remaining_calories = calorie_limit - total_calories_consumed
    result = remaining_calories
    return result

print(solution())