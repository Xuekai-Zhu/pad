def solution():
    # Calculate the total cost before discount
    total_cost = 24 * 7

    # Calculate the amount of the discount
    discount = 0.5 * total_cost

    # Calculate the total cost after discount
    total_cost -= discount

    result = total_cost
    return result

print(solution())