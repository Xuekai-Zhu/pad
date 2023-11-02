def solution():
    """To make yogurt, the company needs milk and fruit. Milk is bought at $1.5 per liter and fruit at $2 per kilogram. To make one batch of yogurt, the company needs 10 liters of milk, and 3 kilograms of fruit. How much does it cost the firm to produce three batches of yogurt?"""
    milk_price = 1.5
    fruit_price = 2
    milk_per_batch = 10
    fruit_per_batch = 3
    total_cost_per_batch = (milk_price * milk_per_batch) + (fruit_price * fruit_per_batch)
    total_cost = total_cost_per_batch * 3
    result = total_cost
    return result

print(solution())