def solution():
    num_shirts = 2
    num_pants = 3
    total_paid = 120
    refund_percent = 0.25  # 25% refund

    # Calculate the total cost of all items
    total_cost = total_paid / (1 - refund_percent)

    # Calculate the cost of one pair of pants
    pants_cost = total_cost / (num_shirts + num_pants)

    # Calculate the cost of one shirt
    shirt_cost = (total_cost - (pants_cost * num_pants)) / num_shirts
    result = shirt_cost
    return result

print(solution())