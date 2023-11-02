def solution():
    dog_food_per_day = 2  # Jaylen's dog eats 2 cups of dog food per day (1 cup in the morning and 1 cup in the evening)
    bag_size = 32  # Jaylen buys a bag of dog food that has 32 cups of dog food

    # Calculate how many days the bag of dog food will last for
    days_of_food = bag_size / dog_food_per_day
    result = days_of_food
    return result

print(solution())