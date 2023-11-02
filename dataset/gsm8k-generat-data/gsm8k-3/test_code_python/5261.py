def solution():
    """Due to a drought, Jerry's household can only use 1000 gallons of water during July. Jerry uses 100 gallons for drinking and cooking and 20 gallons per shower. He wants to fill his pool, which measures 10 feet by 10 feet by 6 feet. If each gallon of water fills 1 cubic foot of the pool, how many showers can Jerry take in July?"""
    # Define the total amount of water Jerry can use in July
    water_budget = 1000

    # Calculate the volume of Jerry's pool
    pool_volume = 10 * 10 * 6

    # Calculate the amount of water needed to fill the pool
    pool_water = pool_volume

    # Calculate the amount of water remaining in Jerry's budget after filling the pool and using water for drinking/cooking
    remaining_water = water_budget - pool_water - 100

    # Calculate the maximum number of showers Jerry can take with the remaining water
    max_showers = remaining_water / 20

    # Display the maximum number of showers Jerry can take
    result = max_showers
    return result

print(solution())