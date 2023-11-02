def solution():
    # Calculate the cost of one personalized backpack
    cost_of_backpack = 20 * (1 - 0.2) + 12  # 20% discount of $20.00, plus $12.00 for monogramming

    # Calculate the total cost of 5 personalized backpacks
    total_cost = cost_of_backpack * 5

    result = total_cost
    return result

print(solution())