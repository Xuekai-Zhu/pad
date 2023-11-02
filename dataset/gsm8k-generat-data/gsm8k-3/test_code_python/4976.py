def solution():
    """There are 10 6-ounces of glasses that are only 4/5 full of water. How many ounces of water are needed to fill to the brim all those 10 glasses?"""
    # Define the size of each glass and the fraction of water it is currently filled with
    GLASS_SIZE = 6 # in ounces
    FRACTION_FILLED = 4/5

    # Calculate the amount of water needed to fill each glass to the brim
    water_needed = GLASS_SIZE - (GLASS_SIZE * FRACTION_FILLED)

    # Calculate the total amount of water needed to fill all 10 glasses to the brim
    total_water_needed = water_needed * 10

    # Display the total amount of water needed
    result = total_water_needed
    return result

print(solution())