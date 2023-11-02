def solution():
    # Calculate the total cost of the dress shirts
    cost_before_tax = 3 * 20  # 3 dress shirts each costing $20
    tax = 0.10 * cost_before_tax  # 10% tax on everything
    total_cost = cost_before_tax + tax

    result = total_cost
    return result

print(solution())