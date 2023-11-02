def solution():
    """Cary is an engineer in charge of designing an irrigation system for three farmers. Farmer Bob grows 3 acres of corn, 9 acres of cotton, and 12 acres of beans. Farmer Brenda grows 6 acres of corn, 7 acres of cotton, and 14 acres of beans. Farmer Bernie grows 2 acres of corn and 12 acres of cotton. If corn takes 20 gallons of water an acre, cotton takes 80 gallons of water an acre, and beans take twice as much water as corn, what percentage of the total water used will go to Farmer Bob's farm?"""
    # Define the water usage per acre for each crop
    CORN_WATER_USAGE = 20
    COTTON_WATER_USAGE = 80
    BEANS_WATER_USAGE = CORN_WATER_USAGE * 2

    # Calculate the total water used for each farmer
    bob_water = (3 * CORN_WATER_USAGE) + (9 * COTTON_WATER_USAGE) + (12 * BEANS_WATER_USAGE)
    brenda_water = (6 * CORN_WATER_USAGE) + (7 * COTTON_WATER_USAGE) + (14 * BEANS_WATER_USAGE)
    bernie_water = (2 * CORN_WATER_USAGE) + (12 * COTTON_WATER_USAGE)

    # Calculate the total water used on all three farms
    total_water = bob_water + brenda_water + bernie_water

    # Calculate the percentage of total water used on Bob's farm
    bob_percentage = (bob_water / total_water) * 100

    result = bob_percentage
    return result

print(solution())