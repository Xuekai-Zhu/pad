def solution():
    # Define the amount of food per meal per dog
    food_per_dog_per_meal = 1.5

    # Calculate the total amount of food per meal
    total_food_per_meal = food_per_dog_per_meal * 2

    # Calculate the total amount of food per day
    total_food_per_day = total_food_per_meal * 3

    # Calculate the total amount of food per day in pounds
    total_food_per_day_in_pounds = total_food_per_day / 2.25

    result = total_food_per_day_in_pounds
    return result

print(solution())