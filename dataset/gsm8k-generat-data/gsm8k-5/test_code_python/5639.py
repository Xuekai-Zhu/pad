def solution():
    num_stadiums = 30  # There are 30 major league baseball stadiums
    cost_per_stadium = 900  # The average cost to travel and see a game at each stadium is $900
    savings_per_year = 1500  # Zach can save $1,500 per year for his stadium trips

    # Calculate the total cost to visit all stadiums
    total_cost = num_stadiums * cost_per_stadium

    # Calculate the number of years it will take for Zach to save enough money
    num_years = total_cost / savings_per_year
    result = num_years
    return result

print(solution())