def solution():
    # Calculate the cost of raising the child for the first 8 years
    first_8_years_cost = 10000 * 8

    # Calculate the cost of raising the child for the next 10 years
    next_10_years_cost = 2 * 10000 * 10

    # Calculate the total cost of raising the child
    total_cost = first_8_years_cost + next_10_years_cost + 250000

    # Calculate John's contribution to the total cost
    john_contribution = total_cost / 2

    result = john_contribution
    return result

print(solution())