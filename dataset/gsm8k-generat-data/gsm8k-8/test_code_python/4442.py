def solution():
    # Calculate the weight Thomas wants to add
    weight_increase = 0.6 * 60
    new_weight = 60 + weight_increase

    # Calculate the number of 2-pound steel ingots needed
    num_ingots = new_weight / 2

    # Calculate the cost of the ingots without discount
    cost = num_ingots * 5

    # Apply the discount if applicable
    if num_ingots > 10:
        discount = 0.2 * cost
        cost -= discount

    result = cost
    return result

print(solution())