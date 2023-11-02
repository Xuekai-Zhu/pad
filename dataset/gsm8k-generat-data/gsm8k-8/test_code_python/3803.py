def solution():
    # Define the variables
    fandoms = 4
    shirts_per_fandom = 5
    shirt_cost = 15
    discount = 0.2
    tax = 0.1

    # Calculate the total cost before discount
    total_cost_before_discount = fandoms * shirts_per_fandom * shirt_cost

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount * (1 - discount)

    # Calculate the total cost with tax
    total_cost_with_tax = total_cost_after_discount * (1 + tax)

    result = total_cost_with_tax
    return result

print(solution())