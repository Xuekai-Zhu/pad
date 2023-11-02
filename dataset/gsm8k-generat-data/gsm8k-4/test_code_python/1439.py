def solution():
    """Gemma ordered four pizzas at $10 each, and she gave a $5 tip to the delivery person. How much change did she get back if she gives one fifty-dollar bill?"""
    # Define the cost of the pizzas and the tip
    pizza_cost = 10
    tip = 5

    # Calculate the total cost of the pizzas and the tip
    total_cost = (pizza_cost * 4) + tip

    # Calculate the amount paid by Gemma
    amount_paid = 50

    # Calculate the change
    change = amount_paid - total_cost

    # return the result
    result = change
    return result

print(solution())