def solution():
    num_stadiums = 30
    cost_per_stadium = 900
    savings_per_year = 1500

    # Calculate the total cost to visit all stadiums
    total_cost = num_stadiums * cost_per_stadium

    # Calculate the number of years it will take Zach to save enough money
    num_years = total_cost / savings_per_year
    result = num_years
    return result

print(solution())