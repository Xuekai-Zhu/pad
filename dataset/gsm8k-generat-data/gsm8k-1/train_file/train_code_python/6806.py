def solution():
    """To make yogurt, the company needs milk and fruit. Milk is bought at $1.5 per liter and fruit at $2 per kilogram. To make one batch of yogurt, the company needs 10 liters of milk, and 3 kilograms of fruit. How much does it cost the firm to produce three batches of yogurt?"""
    milk_cost = 1.5
    fruit_cost = 2
    milk_needed = 10
    fruit_needed = 3
    batches = 3
    total_milk_cost = milk_needed * milk_cost * batches
    total_fruit_cost = fruit_needed * fruit_cost * batches
    total_cost = total_milk_cost + total_fruit_cost
    result = total_cost
    return result

print(solution())