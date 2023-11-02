def solution():
    """Melody has three dogs. Each dog eats 1/2 of a pound of dog food twice a day. If Melody bought 30 pounds of dog food, how many pounds of dog food are left after a week?"""
    # Define the number of dogs and the amount of food they eat per day
    num_dogs = 3
    food_per_dog_per_day = 0.5

    # Define the amount of food Melody bought
    total_food = 30

    # Calculate the total amount of food the dogs eat per day
    total_food_per_day = num_dogs * food_per_dog_per_day * 2

    # Calculate the total amount of food the dogs eat in a week
    total_food_per_week = total_food_per_day * 7

    # Calculate the amount of food left after a week
    food_left = total_food - total_food_per_week

    # Return the result
    result = food_left
    return result

print(solution())