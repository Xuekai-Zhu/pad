def solution():
    """Voldemort had his dinner and ate a piece of cake that has 110 calories. He also ate 1 pack of chips that contained 310 calories and drank a 500 ml bottle of coke that has 215 calories. His caloric intake for breakfast and lunch is 560 and 780 calories, respectively. If he has a 2500 calorie intake limit per day, how many calories can he still take?"""
    # Define the number of calories for each food item
    CAKE_CALORIES = 110
    CHIPS_CALORIES = 310
    COKE_CALORIES = 215
    BREAKFAST_CALORIES = 560
    LUNCH_CALORIES = 780
    DAILY_LIMIT = 2500

    # Calculate the total number of calories consumed
    total_calories = CAKE_CALORIES + CHIPS_CALORIES + COKE_CALORIES + BREAKFAST_CALORIES + LUNCH_CALORIES

    # Calculate the number of calories Voldemort can still take
    remaining_calories = DAILY_LIMIT - total_calories

    # Display the number of calories Voldemort can still take
    result = remaining_calories
    return result

print(solution())