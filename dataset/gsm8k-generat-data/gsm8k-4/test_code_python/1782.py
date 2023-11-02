def solution():
    """In a restaurant, a burger costs $9, and a pizza twice as much. How much would cost one pizza and three burgers?"""
    # Define the cost of a burger
    burger_cost = 9

    # Calculate the cost of a pizza
    pizza_cost = burger_cost * 2

    # Calculate the total cost of one pizza and three burgers
    total_cost = (pizza_cost * 1) + (burger_cost * 3)

    result = total_cost
    return result

print(solution())