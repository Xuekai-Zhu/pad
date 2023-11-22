def solution():
    
    # Define the total cost of the pizzas and the cost of the two of them
    total_cost = 64
    two_pizza_cost = 30

    # Calculate the cost of the other two pizzas
    other_pizza_cost = total_cost - two_pizza_cost

    # Calculate the cost of each of the other two pizzas
    cost_each_other_two = other_pizza_cost / 2

    # Display the cost of each of the other two pizzas
    result = cost_each_other_two
    return result

print(solution())