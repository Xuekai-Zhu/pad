def solution():
    # Calculate the amount of food the mom dog eats each day
    mom_daily_food = 1.5 * 3

    # Calculate the amount of food each puppy eats each day
    puppy_daily_food = 0.5 * 2 * 5

    # Calculate the total amount of food needed each day
    total_daily_food = mom_daily_food + puppy_daily_food

    # Calculate the total amount of food needed for 6 days
    total_food_needed = total_daily_food * 6

    result = total_food_needed
    return result

print(solution())