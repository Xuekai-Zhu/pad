def solution():
    # Calculate the remaining budget after accounting for subway fare and previous purchases
    budget = 50 - (2 * 3.5) - 10 - (0.5 * 10)

    # Calculate the cost per apple
    apple_cost = 14 / 12

    # Calculate the maximum number of apples Brian can buy with his remaining budget
    max_apples = budget / apple_cost

    # Round down to the nearest whole number
    max_apples = int(max_apples)

    result = max_apples
    return result

print(solution())