def solution():
    milk_price_per_batch = 1.5 * 10  # Milk cost for one batch of yogurt
    fruit_price_per_batch = 2 * 3  # Fruit cost for one batch of yogurt
    total_price_per_batch = milk_price_per_batch + fruit_price_per_batch  # Total cost for one batch of yogurt
    cost_of_three_batches = total_price_per_batch * 3  # Total cost for three batches of yogurt
    result = cost_of_three_batches
    return result

print(solution())