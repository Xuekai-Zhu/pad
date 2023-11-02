def solution():
    # Calculate the cost of toilet paper and paper towels
    tp_cost = 1.5 * 10  # 10 rolls of toilet paper cost $1.5 each
    pt_cost = 2 * 7  # 7 rolls of paper towels cost $2 each

    # Calculate the cost of tissues
    total_cost = tp_cost + pt_cost + 3*x  # x is the cost of one box of tissues
    x = (35 - tp_cost - pt_cost) / 3  # solve for x using the total cost equation

    result = x
    return result

print(solution())