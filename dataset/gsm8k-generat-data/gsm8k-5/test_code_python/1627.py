def solution():
    # Calculate the amount of water filled by the first hose
    first_hose_water = 50 * 3  # 50 gallons per hour for 3 hours

    # Calculate the amount of water filled by the second hose
    second_hose_water = 70 * 2  # 70 gallons per hour for 2 more hours

    # Calculate the total amount of water filled in the pool
    total_water = first_hose_water + second_hose_water

    result = total_water
    return result

print(solution())