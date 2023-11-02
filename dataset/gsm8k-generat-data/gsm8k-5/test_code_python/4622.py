def solution():
    cost_of_televisions = 5 * 50  # Annie spent $250 on televisions
    total_cost = 260  # Annie spent a total of $260
    cost_of_figurines = total_cost - cost_of_televisions  # Find the cost of figurines

    # Calculate the cost of a single figurine
    cost_per_figurine = cost_of_figurines / 10
    result = cost_per_figurine
    return result

print(solution())