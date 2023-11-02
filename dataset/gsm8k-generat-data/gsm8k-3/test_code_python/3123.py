def solution():
    """Madeline wants to drink 100 ounces of water in a day. Her water bottle can hold 12 ounces of water. She refills her water bottle 7 times. How much more water does she need to drink?"""
    # Define the total amount of water Madeline wants to drink
    total_water = 100

    # Define the amount of water Madeline drinks from her water bottle
    bottle_size = 12
    refills = 7
    water_from_bottle = bottle_size * refills

    # Calculate the amount of water Madeline still needs to drink
    remaining_water = total_water - water_from_bottle

    # Display the amount of water Madeline still needs to drink
    result = remaining_water
    return result

print(solution())