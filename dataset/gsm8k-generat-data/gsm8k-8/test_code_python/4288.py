def solution():
    # Calculate the cost of the hamburgers
    hamburger_cost = 2 * 5

    # Calculate the cost of the cola bottles
    cola_cost = 3 * 2

    # Calculate the total cost before discount
    total_cost = hamburger_cost + cola_cost

    # Apply the discount
    total_cost -= 4

    result = total_cost
    return result

print(solution())