def solution():
    """To make yogurt, the company needs milk and fruit. Milk is bought at $1.5 per liter and fruit at $2 per kilogram. To make one batch of yogurt, the company needs 10 liters of milk, and 3 kilograms of fruit. How much does it cost the firm to produce three batches of yogurt?"""
    # Define the prices of milk and fruit
    milk_price = 1.5
    fruit_price = 2

    # Define the quantities of milk and fruit needed for one batch of yogurt
    milk_per_batch = 10
    fruit_per_batch = 3

    # Calculate the total cost of milk and fruit for three batches of yogurt
    total_milk_cost = milk_price * milk_per_batch * 3
    total_fruit_cost = fruit_price * fruit_per_batch * 3

    # Calculate the total cost of producing three batches of yogurt
    total_cost = total_milk_cost + total_fruit_cost

    # return the result
    result = total_cost
    return result

print(solution())