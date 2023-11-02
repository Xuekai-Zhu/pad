def solution():
    # Calculate the cost for first 3 years
    cost_3_years = 300 * 12 * 3  # $300 per month, 12 months per year, for first 3 years

    # Calculate the cost for next 2 years with increased rent
    cost_2_years = 350 * 12 * 2  # $350 per month, 12 months per year, for next 2 years

    # Calculate the total cost for 5 years
    total_cost = cost_3_years + cost_2_years
    result = total_cost
    return result

print(solution())