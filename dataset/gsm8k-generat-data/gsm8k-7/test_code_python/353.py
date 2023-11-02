def solution():
    num_furniture = 150
    cost_per_furniture = 134
    total_paid = 20700

    # Calculate the total cost of all furniture
    total_cost = num_furniture * cost_per_furniture

    # Calculate the difference between the total cost and the amount paid
    refund_amount = total_paid - total_cost
    result = refund_amount
    return result

print(solution())