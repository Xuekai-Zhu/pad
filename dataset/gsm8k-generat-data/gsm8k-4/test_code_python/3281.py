def solution():
    """Jaylen’s dog eats 1 cup of dog food in the morning and 1 cup of dog food in the evening. If she buys a bag that has 32 cups of dog food, how many days can she feed her dog with it?"""
    # Define the amount of dog food consumed by the dog in one day
    daily_consumption = 2

    # Define the total amount of dog food in the bag
    total_dog_food = 32

    # Calculate the number of days the bag will last
    days = total_dog_food / daily_consumption

    # Return the result
    result = days
    return result

print(solution())