def solution():
    num_pineapples_per_dozen = 12
    pineapple_price = 1.25
    total_shipping_cost = 21.0

    # Calculate the total cost of all pineapples
    total_pineapple_cost = num_pineapples_per_dozen * pineapple_price

    # Calculate the total number of pineapples
    total_pineapples = total_shipping_cost / (total_pineapple_cost)

    # Calculate the cost per pineapple
    cost_per_pineapple = total_pineapple_cost / num_pineapples_per_dozen
    result = round(cost_per_pineapple, 2)
    return result

print(solution())