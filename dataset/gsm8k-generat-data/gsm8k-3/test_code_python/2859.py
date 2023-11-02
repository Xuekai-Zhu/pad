def solution():
    """Allen ordered five boxes of pizza, which cost $7 each box. He then gave a tip which amounts to 1/7 of the total cost of his order. If he gave the delivery man $100, how much change did he receive?"""
    # Define the cost per box of pizza
    PIZZA_PRICE = 7

    # Calculate the total cost of the pizzas
    total_cost = 5 * PIZZA_PRICE

    # Calculate the amount of the tip
    tip = total_cost / 7

    # Calculate the total amount paid, including the tip
    total_paid = total_cost + tip

    # Calculate the change
    change = 100 - total_paid

    # Display the change
    result = change
    return result

print(solution())