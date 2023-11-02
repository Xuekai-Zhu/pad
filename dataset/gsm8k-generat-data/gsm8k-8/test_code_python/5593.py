def solution():
    # Calculate the new prices after inflation
    lumber_price = 450 * 1.2
    nails_price = 30 * 1.1
    fabric_price = 80 * 1.05

    # Calculate the total cost after inflation
    total_cost_now = lumber_price + nails_price + fabric_price

    # Calculate the original total cost
    original_total_cost = 450 + 30 + 80

    # Calculate the difference between the two costs
    cost_difference = total_cost_now - original_total_cost

    result = cost_difference
    return result

print(solution())