def solution():
    # Calculate the cost of the items bought for James and Jamie
    cost_James = 40 + 2*x  # cost of James' coat and two pairs of jeans
    cost_Jamie = 30  # cost of Jamie's shoes

    # Calculate the total cost of the items
    total_cost = cost_James + cost_Jamie

    # Solve for x
    x = (total_cost - 70) / 2  # total_cost = cost_James + cost_Jamie = 40 + 2*x + 30

    result = x
    return result

print(solution())