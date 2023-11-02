def solution():
    """Harry is ordering pizza. A large pizza is 14. It costs $2 per topping. He orders 2 large pizzas, each with 3 toppings. He then adds a 25% tip. What is the total cost?"""
    # Define the cost of a large pizza and the cost per topping
    LARGE_PIZZA_COST = 14
    TOPPING_COST = 2

    # Calculate the cost of the pizzas and toppings
    pizza_cost = 2 * LARGE_PIZZA_COST
    topping_cost = 2 * 3 * TOPPING_COST

    # Calculate the subtotal
    subtotal = pizza_cost + topping_cost

    # Add the tip
    tip = 0.25 * subtotal
    total_cost = subtotal + tip

    result = total_cost
    return result

print(solution())