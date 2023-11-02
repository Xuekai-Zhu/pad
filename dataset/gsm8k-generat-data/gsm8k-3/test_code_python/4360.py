def solution():
    """Ursula went to the store and bought butter, bread, a package of cheese, and tea. The bread was 2 times cheaper than the butter, while the price of the butter was 80% of the price of cheese. Tea was the most expensive and cost twice the price of a package of cheese. If the tea cost $10, how much did Ursula pay for her purchases?"""
    # Define the cost of tea and its ratio to the cost of cheese
    TEA_COST = 10
    CHEESE_RATIO = 0.5

    # Calculate the cost of cheese
    cheese_cost = TEA_COST * CHEESE_RATIO

    # Calculate the cost of bread and butter
    butter_cost = cheese_cost * 1.25
    bread_cost = butter_cost * 0.5

    # Calculate the total cost
    total_cost = butter_cost + bread_cost + cheese_cost + TEA_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())