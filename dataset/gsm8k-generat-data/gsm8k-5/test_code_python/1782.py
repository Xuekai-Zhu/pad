def solution():
    burger_cost = 9  # A burger costs $9
    pizza_cost = 2 * burger_cost  # A pizza costs twice as much as a burger
    num_burgers = 3  # Three burgers

    # Calculate the total cost of three burgers
    total_burger_cost = burger_cost * num_burgers

    # Calculate the cost of one pizza
    pizza_cost_one = pizza_cost

    # Calculate the total cost of one pizza and three burgers
    total_cost = pizza_cost_one + total_burger_cost
    result = total_cost
    return result

print(solution())