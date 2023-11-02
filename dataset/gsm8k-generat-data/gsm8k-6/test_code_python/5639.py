def solution():
    # Calculate the total cost for Zach to visit all 30 stadiums
    total_cost = 30 * 900  # $900 per stadium

    # Calculate the number of years it will take Zach to save enough money
    years = total_cost // 1500  # $1,500 saved per year
    if total_cost % 1500 != 0:
        years += 1
    result = years
    return result

print(solution())