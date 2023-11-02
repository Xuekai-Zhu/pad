def solution():
    # Calculate the cost of raising the child for the first 8 years
    cost_first_8_years = 10000 * 8

    # Calculate the cost of raising the child from age 9 to 18
    cost_next_9_years = 2 * 10000 * (18 - 8)

    # Calculate the total cost of raising the child
    total_cost = cost_first_8_years + cost_next_9_years + 250000

    # Calculate John's contribution to the total cost
    john_contribution = 0.5 * total_cost
    result = john_contribution
    return result

print(solution())