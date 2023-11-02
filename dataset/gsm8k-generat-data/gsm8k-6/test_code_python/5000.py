def solution():
    # Calculate the total cost of Ray's groceries before the 10% discount
    total_cost = 5 + 3.5 + 4*2 + 3.5

    # Calculate the amount of the discount
    discount = 0.1 * total_cost

    # Calculate the total cost of Ray's groceries after the discount
    total_cost_after_discount = total_cost - discount

    result = total_cost_after_discount
    return result

print(solution())