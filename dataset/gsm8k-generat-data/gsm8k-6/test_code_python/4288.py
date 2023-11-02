def solution():
    # Calculate the total cost of hamburgers and colas
    hamburgers_cost = 2 * 5
    colas_cost = 3 * 2
    total_cost = hamburgers_cost + colas_cost

    # Apply the discount coupon
    total_cost -= 4

    result = total_cost
    return result

print(solution())