def solution():
    # Calculate the cost per year for each coat
    cost_per_year_expensive = 300 / 15  # $300 over 15 years
    cost_per_year_cheap = 120 / 5  # $120 over 5 years

    # Calculate the total cost over 30 years for each coat
    total_cost_expensive = cost_per_year_expensive * 30
    total_cost_cheap = cost_per_year_cheap * 30

    # Calculate the savings by buying the more expensive coat
    savings = total_cost_cheap - total_cost_expensive
    result = savings
    return result

print(solution())