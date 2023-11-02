def solution():
    # Calculate the cost of the first 6 months of the service
    cost_first_6_months = 8 * 6  # $8 per month for 6 months

    # Calculate the cost of the next 8 months of the service
    cost_next_8_months = 12 * 8  # $12 per month for 8 months

    # Calculate the cost of the service after 8 months of the normal rate
    cost_next_8_months = 14 * 8  # $14 per month for 8 months

    # Calculate the total cost of the service
    total_cost = cost_first_6_months + cost_next_8_months + cost_next_14_months
    result = total_cost
    return result

print(solution())