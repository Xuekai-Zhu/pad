def solution():
    """Jaylen’s dog eats 1 cup of dog food in the morning and 1 cup of dog food in the evening. If she buys a bag that has 32 cups of dog food, how many days can she feed her dog with it?"""
    daily_dog_food_cups = 2
    bag_size = 32
    days_of_food = bag_size / daily_dog_food_cups
    result = days_of_food
    return result

print(solution())