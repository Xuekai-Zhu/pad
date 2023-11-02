def solution():
    # Calculate the cost of a dozen pineapples
    cost_dozen = 12 * 1.25

    # Subtract the cost of pineapples from the total cost to get the shipping cost
    shipping_cost = 21 - cost_dozen

    # Divide the shipping cost by the number of pineapples to get the cost per pineapple
    cost_per_pineapple = shipping_cost / 12
    result = cost_per_pineapple
    return result

print(solution())