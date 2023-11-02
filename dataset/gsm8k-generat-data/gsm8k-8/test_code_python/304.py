def solution():
    # Calculate the total water needed for each crop type for each farmer
    bob_water = 3 * 20 + 9 * 80 + 12 * 40
    brenda_water = 6 * 20 + 7 * 80 + 14 * 40
    bernie_water = 2 * 20 + 12 * 80

    # Calculate the total water needed for all three farmers
    total_water = bob_water + brenda_water + bernie_water

    # Calculate the percentage of total water used by Farmer Bob
    bob_percentage = bob_water / total_water * 100
    result = bob_percentage
    return result

print(solution())