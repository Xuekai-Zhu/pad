def solution():
    num_tshirts = 3
    cost_per_tshirt = 20
    cost_pants = 50

    # Calculate the total cost for the t-shirts
    total_tshirt_cost = num_tshirts * cost_per_tshirt

    # Calculate the total cost of the purchase
    total_cost = total_tshirt_cost + cost_pants
    result = total_cost
    return result

print(solution())