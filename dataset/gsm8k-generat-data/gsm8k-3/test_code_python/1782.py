def solution():
    """In a restaurant, a burger costs $9, and a pizza twice as much. How much would cost one pizza and three burgers?"""
    # Define the cost of a burger and pizza
    BURGER_COST = 9
    PIZZA_COST = 2 * BURGER_COST

    # Calculate the total cost of one pizza and three burgers
    total_cost = (3 * BURGER_COST) + PIZZA_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())