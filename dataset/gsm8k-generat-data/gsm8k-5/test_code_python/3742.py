def solution():
    total_cost = 120  # Total cost of 2 shirts and 3 pairs of pants
    num_shirts = 2
    num_pants = 3

    # Calculate the cost per item before returning the pants
    original_cost_per_item = total_cost / (num_shirts + num_pants)

    # Calculate the total cost of just the shirts
    total_cost_shirts = num_shirts * original_cost_per_item

    # Calculate the amount refunded after returning the pants
    refund_amount = 0.25 * total_cost_per_item * num_pants

    # Calculate the final cost of just the shirts after returning the pants
    final_cost_shirts = total_cost_shirts - refund_amount

    # Calculate the price of one shirt
    price_shirt = final_cost_shirts / num_shirts
    result = price_shirt
    return result

print(solution())