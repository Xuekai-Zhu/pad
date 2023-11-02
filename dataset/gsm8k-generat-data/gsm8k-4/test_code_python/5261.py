def solution():
    """Due to a drought, Jerry's household can only use 1000 gallons of water during July. Jerry uses 100 gallons for drinking and cooking and 20 gallons per shower. He wants to fill his pool, which measures 10 feet by 10 feet by 6 feet. If each gallon of water fills 1 cubic foot of the pool, how many showers can Jerry take in July?"""
    
    # Define the total available water in gallons
    total_water_gallons = 1000

    # Define the water usage for drinking and cooking
    drinking_cooking_gallons = 100

    # Define the pool dimensions and calculate the total water needed to fill it
    pool_length = 10
    pool_width = 10
    pool_depth = 6
    pool_total_water_gallons = pool_length * pool_width * pool_depth

    # Calculate the remaining water available for showering
    showering_water_gallons = total_water_gallons - drinking_cooking_gallons - pool_total_water_gallons

    # Calculate the maximum number of showers possible with the remaining water
    showers_possible = showering_water_gallons / 20

    result = int(showers_possible)
    return result

print(solution())