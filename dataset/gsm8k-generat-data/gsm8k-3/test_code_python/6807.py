def solution():
    """To make yogurt, the company needs milk and fruit. Milk is bought at $1.5 per liter and fruit at $2 per kilogram. To make one batch of yogurt, the company needs 10 liters of milk, and 3 kilograms of fruit. How much does it cost the firm to produce three batches of yogurt?"""
    # Define the cost of milk and fruit
    MILK_COST = 1.5
    FRUIT_COST = 2

    # Define the amounts of milk and fruit needed for one batch of yogurt
    MILK_PER_BATCH = 10
    FRUIT_PER_BATCH = 3

    # Calculate the cost to make one batch of yogurt
    batch_cost = MILK_PER_BATCH * MILK_COST + FRUIT_PER_BATCH * FRUIT_COST

    # Calculate the cost to make three batches of yogurt
    total_cost = 3 * batch_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())