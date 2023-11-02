def solution():
    """Remi wants to drink more water. He has a refillable water bottle that holds 20 ounces of water. That week Remi refills the bottle 3 times a day and drinks the whole bottle each time except for twice when he accidentally spills 5 ounces the first time and 8 ounces the second time. In 7 days how many ounces of water does Remi drink?"""
    # Define the capacity of Remi's water bottle
    BOTTLE_CAPACITY = 20

    # Define the number of times Remi refills his bottle each day
    REFILL_TIMES = 3

    # Define the amount of water Remi spills
    SPILL_1 = 5
    SPILL_2 = 8

    # Calculate the total amount of water Remi drinks each day
    water_per_day = (BOTTLE_CAPACITY * REFILL_TIMES) - SPILL_1 - SPILL_2

    # Calculate the total amount of water Remi drinks in 7 days
    total_water = water_per_day * 7

    # Return the result
    result = total_water
    return result

print(solution())