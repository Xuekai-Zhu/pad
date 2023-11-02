def solution():
    # Calculate the total cost of Jackie's order
    shampoo_cost = 2*10  # cost of two bottles of shampoo
    lotion_cost = 3*6  # cost of three bottles of lotion
    total_cost = shampoo_cost + lotion_cost

    # Calculate the amount of money Jackie needs to spend to be eligible for free shipping
    remaining_cost = 50 - total_cost
    result = remaining_cost
    return result

print(solution())