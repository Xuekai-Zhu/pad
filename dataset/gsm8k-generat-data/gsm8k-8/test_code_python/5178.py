def solution():
    # Define the weight of a small apple
    apple_weight = 1 / 4

    # Calculate the amount of apples needed for two weeks, sharing half of each apple
    apples_needed = (7 * 2) * 2 * (1 / 2)  # 7 days in a week, 2 weeks, 2 apples shared each day

    # Calculate the total weight of apples needed
    total_weight = apples_needed * apple_weight

    # Calculate the total cost based on the current price of apples
    cost = total_weight * 2

    result = cost
    return result

print(solution())