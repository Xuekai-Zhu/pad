def solution():
    pineapples_per_dozen = 12  # Steve and Georgia buy a dozen pineapples
    cost_per_pineapple = 1.25  # Each pineapple costs $1.25
    total_cost = pineapples_per_dozen * cost_per_pineapple  # Total cost for a dozen pineapples

    # Calculate the cost per pineapple after adding shipping charges
    cost_per_pineapple_with_shipping = (total_cost + 21) / pineapples_per_dozen
    result = cost_per_pineapple_with_shipping
    return result

print(solution())