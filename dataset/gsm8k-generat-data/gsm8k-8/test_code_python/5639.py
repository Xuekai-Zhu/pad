def solution():
    # Calculate the total cost to visit all 30 stadiums
    total_cost = 30 * 900

    # Calculate the number of years it will take Zach to save enough money
    years_to_save = total_cost / 1500

    # Round up to the nearest whole number of years
    result = math.ceil(years_to_save)
    return result

print(solution())