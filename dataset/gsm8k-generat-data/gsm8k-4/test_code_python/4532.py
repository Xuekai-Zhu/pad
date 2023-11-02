def solution():
    """
    Mr. Reyansh has a dairy farm with 40 cows. Each cow on the farm drinks 80 liters of water daily. 
    He also has a sheep ranch with 10 times the number of cows, with each sheep drinking 1/4 times as 
    much water as a cow does. How many liters of water does Mr. Reyansh use to water all of his animals in a week?
    """
    # Define the number of cows and sheep
    cows = 40
    sheep = cows * 10

    # Calculate the total water used by the cows
    cow_water = cows * 80

    # Calculate the water used by each sheep
    sheep_water = 1/4 * 80

    # Calculate the total water used by the sheep
    total_sheep_water = sheep * sheep_water

    # Calculate the total water used by all the animals in a week
    total_water = (cow_water + total_sheep_water) * 7

    # Return the result
    result = total_water
    return result

print(solution())