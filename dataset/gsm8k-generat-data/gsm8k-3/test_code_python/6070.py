def solution():
    """Luigi bought four pizzas for $80. Each pizza was cut into 5 pieces. How much did each piece of pizza cost, in dollars?"""
    # Define the number of pizzas and total cost
    num_pizzas = 4
    total_cost = 80

    # Calculate the cost per pizza
    pizza_cost = total_cost / num_pizzas

    # Calculate the cost per piece of pizza
    cost_per_piece = pizza_cost / 5

    # Display the cost per piece of pizza
    result = cost_per_piece
    return result

print(solution())