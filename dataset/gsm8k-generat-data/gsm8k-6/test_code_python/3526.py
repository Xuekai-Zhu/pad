def solution():
    # Calculate the cost of 10 apples and 5 oranges
    cost_apples = 200  # 10 apples for $2, so 1 apple costs 20 cents
    cost_oranges = 150  # 5 oranges for $1.50, so 1 orange costs 30 cents

    # Buy 12 of the cheaper fruit
    if cost_apples < cost_oranges:
        cost_cheaper_fruit = cost_apples
    else:
        cost_cheaper_fruit = cost_oranges
    total_cost = cost_cheaper_fruit * 12
    result = total_cost
    return result

print(solution())