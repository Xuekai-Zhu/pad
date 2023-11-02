def solution():
    # Calculate the total water used for each crop
    corn_water = 20
    cotton_water = 80
    beans_water = 2 * corn_water

    # Calculate the total water used for each farmer
    bob_water = (3 * corn_water) + (9 * cotton_water) + (12 * beans_water)
    brenda_water = (6 * corn_water) + (7 * cotton_water) + (14 * beans_water)
    bernie_water = (2 * corn_water) + (12 * cotton_water)

    # Calculate the total water used for all three farmers
    total_water = bob_water + brenda_water + bernie_water

    # Calculate the percentage of total water used for Farmer Bob's farm
    bob_percentage = (bob_water / total_water) * 100
    result = bob_percentage
    return result

print(solution())