def solution():
    """Harry is ordering pizza. A large pizza is $14. It costs $2 per topping. He orders 2 large pizzas, each with 3 toppings. He then adds a 25% tip. What is the total cost?"""
    # Define the cost of a large pizza and the cost per topping
    LARGE_PIZZA_COST = 14
    TOPPING_COST = 2

    # Calculate the cost of the pizzas
    pizza_cost = 2 * LARGE_PIZZA_COST

    # Calculate the cost of the toppings
    topping_cost = 2 * 3 * TOPPING_COST

    # Calculate the total cost before tip
    total_cost_before_tip = pizza_cost + topping_cost

    # Calculate the tip amount
    tip_amount = total_cost_before_tip * 0.25

    # Calculate the total cost including tip
    total_cost = total_cost_before_tip + tip_amount

    # Display the total cost
    result = total_cost
    return result

print(solution())