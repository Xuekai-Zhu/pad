def solution():
    """Jaylen’s dog eats 1 cup of dog food in the morning and 1 cup of dog food in the evening.  If she buys a bag that has 32 cups of dog food, how many days can she feed her dog with it?"""
    
    # Determine the amount of dog food consumed by the dog per day
    daily_consumption = 1 + 1
    
    # Determine the number of days the bag of dog food will last
    bag_size = 32
    days = bag_size / daily_consumption
    
    # Return the number of days
    result = days
    return result

print(solution())