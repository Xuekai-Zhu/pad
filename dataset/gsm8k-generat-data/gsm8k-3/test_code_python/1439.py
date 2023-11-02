def solution():
    """Gemma ordered four pizzas at $10 each, and she gave a $5 tip to the delivery person. How much change did she get back if she gives one fifty-dollar bill?"""
    # Define the cost per pizza and the tip amount
    PIZZA_COST = 10
    TIP_AMOUNT = 5

    # Calculate the total cost of the pizzas and the tip
    total_cost = PIZZA_COST * 4 + TIP_AMOUNT

    # Calculate the change Gemma will receive from a $50 bill
    change = 50 - total_cost

    # Display the change Gemma will receive
    result = change
    return result

print(solution())