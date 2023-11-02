def solution():
    # Calculate the total cost before discount
    total_cost = 20 + 20 + 2*2.5 + 15 + 20 + 20 + 15  

    # Calculate the discount amount
    discount = 0.2 * total_cost

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost - discount
    result = total_cost_after_discount
    return result

print(solution())