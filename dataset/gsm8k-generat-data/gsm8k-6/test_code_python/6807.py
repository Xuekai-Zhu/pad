def solution():
    # Calculate the cost to produce one batch of yogurt
    milk_cost = 10 * 1.5  # 10 liters of milk at $1.5 per liter
    fruit_cost = 3 * 2  # 3 kilograms of fruit at $2 per kilogram
    total_cost = milk_cost + fruit_cost  # total cost to produce one batch

    # Calculate the cost to produce three batches of yogurt
    three_batches_cost = total_cost * 3
    result = three_batches_cost
    return result

print(solution())