def solution():
    cost_per_pound = 3
    minimum_purchase = 15
    total_cost = 105

    # Calculate the cost of the minimum purchase
    minimum_cost = minimum_purchase * cost_per_pound

    # Calculate the excess cost paid by Baxter
    excess_cost = total_cost - minimum_cost

    # Calculate the pounds of peanuts purchased over the minimum
    pounds_over_minimum = excess_cost / cost_per_pound
    result = pounds_over_minimum
    return result

print(solution())