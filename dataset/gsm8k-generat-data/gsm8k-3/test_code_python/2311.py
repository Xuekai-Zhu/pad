def solution():
    """Melody has three dogs. Each dog eats 1/2 of a pound of dog food twice a day. If Melody bought 30 pounds of dog food, how many pounds of dog food are left after a week?"""
    # Define the amount of dog food each dog eats per day
    dog_food_per_day = 1

    # Calculate the total amount of dog food each dog eats in a week
    dog_food_per_week = dog_food_per_day * 7

    # Calculate the total amount of dog food Melody's three dogs eat in a week
    total_dog_food_per_week = dog_food_per_week * 3

    # Calculate the remaining amount of dog food after a week
    remaining_dog_food = 30 - total_dog_food_per_week

    # Display the remaining amount of dog food
    result = remaining_dog_food
    return result

print(solution())