def solution():
    # Define the amount of food per feeding and per day
    food_per_feeding_1 = 0.25
    food_per_feeding_2 = 0.5
    feedings_per_day_1 = 3
    feedings_per_day_2 = 2

    # Define the number of days for each feeding schedule
    days_1 = 14
    days_2 = 14

    # Calculate the total amount of food for each feeding schedule
    total_food_1 = food_per_feeding_1 * feedings_per_day_1 * days_1
    total_food_2 = food_per_feeding_2 * feedings_per_day_2 * days_2

    # Add the amount of food fed today
    total_food = total_food_1 + total_food_2 + 0.5

    result = total_food
    return result

print(solution())