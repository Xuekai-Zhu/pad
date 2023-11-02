def solution():
    cost_per_pound = 3  # Peanuts cost $3 per pound
    minimum_purchase = 15  # Minimum purchase is 15 pounds
    total_cost = 105  # Baxter spent $105 on peanuts

    # Calculate the total number of pounds of peanuts Baxter bought
    total_pounds = total_cost / cost_per_pound

    # Calculate the number of pounds over the minimum purchase
    pounds_over_minimum = total_pounds - minimum_purchase
    result = pounds_over_minimum
    return result

print(solution())