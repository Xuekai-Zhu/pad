def solution():
    """A desert garden’s sprinkler system runs twice a day during the cool morning and evening hours. It waters the garden with four liters of water in the morning and six liters in the evening. How many days does it take the sprinkler system to use 50 liters of water?"""
    # Define the water usage per day
    water_usage_per_day = 4 + 6

    # Calculate the number of days it takes to use 50 liters of water
    days = 50 // water_usage_per_day

    result = days
    return result

print(solution())