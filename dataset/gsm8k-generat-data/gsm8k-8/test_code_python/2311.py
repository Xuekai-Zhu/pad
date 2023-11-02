def solution():
    # Define the amount of food each dog eats per day
    daily_food_per_dog = 1/2 * 2

    # Calculate the total amount of food the dogs eat per day
    total_daily_food = daily_food_per_dog * 3

    # Calculate the total amount of food the dogs eat in a week
    total_weekly_food = total_daily_food * 7

    # Calculate how much food is left after a week
    food_left = 30 - total_weekly_food
    result = food_left
    return result

print(solution())