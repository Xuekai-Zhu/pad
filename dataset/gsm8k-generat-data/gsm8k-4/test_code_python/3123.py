def solution():
    """Madeline wants to drink 100 ounces of water in a day. Her water bottle can hold 12 ounces of water. She refills her water bottle 7 times. How much more water does she need to drink?"""
    # Define the total amount of water Madeline can drink from the water bottle
    water_bottle_capacity = 12

    # Calculate the total amount of water Madeline can drink from refilling her water bottle 7 times
    total_water_from_refill = water_bottle_capacity * 7

    # Calculate the amount of water Madeline still needs to drink
    remaining_water = 100 - total_water_from_refill

    # return the result
    result = remaining_water
    return result

print(solution())