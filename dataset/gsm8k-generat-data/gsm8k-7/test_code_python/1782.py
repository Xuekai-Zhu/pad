def solution():
    burger_cost = 9
    pizza_cost = 2 * burger_cost  # twice as much as a burger
    num_burgers = 3

    # Calculate the cost of one pizza and three burgers
    total_cost = pizza_cost + (num_burgers * burger_cost)
    result = total_cost
    return result

print(solution())