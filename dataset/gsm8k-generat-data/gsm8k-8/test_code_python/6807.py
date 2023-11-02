def solution():
    # Define the cost of ingredients per batch of yogurt
    milk_cost = 1.5 * 10
    fruit_cost = 2 * 3
    total_cost_per_batch = milk_cost + fruit_cost

    # Calculate the cost of producing three batches of yogurt
    total_cost = 3 * total_cost_per_batch
    result = total_cost
    return result

print(solution())