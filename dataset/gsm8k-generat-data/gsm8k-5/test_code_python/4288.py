def solution():
    cost_of_hamburgers = 2 * 5  # Wilson buys 2 hamburgers for $5 each
    cost_of_colas = 3 * 2  # Wilson buys 3 bottles of cola for $2 each
    total_cost = cost_of_hamburgers + cost_of_colas  # Calculate the total cost without the discount
    total_cost -= 4  # Subtract the discount of $4
    result = total_cost
    return result

print(solution())