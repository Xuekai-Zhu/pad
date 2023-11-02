def solution():
    # Calculate the total cost of Jimmy's shorts
    cost_Jimmy = 3 * 15

    # Calculate the total cost of Irene's shirts
    cost_Irene = 5 * 17

    # Calculate the total cost before discount
    total_cost = cost_Jimmy + cost_Irene

    # Calculate the discount amount
    discount = 0.1 * total_cost

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost - discount

    result = total_cost_after_discount
    return result

print(solution())