def solution():
    # Calculate the total amount of dog food in grams
    total_food_in_grams = 2 * 50 * 1000

    # Calculate the total amount of food needed per day for all dogs
    total_food_per_day = 4 * 250 * 2

    # Calculate the number of days the food will last
    days_of_food = total_food_in_grams / total_food_per_day

    result = days_of_food
    return result

print(solution())