def solution():
    # Define the cost of the pizza and toppings
    pizza_cost = 10
    topping1_cost = 2
    topping2_cost = 1
    topping3_cost = 0.5

    # Calculate the total cost of the toppings
    topping_cost = topping1_cost + (2 * topping2_cost) + (4 * topping3_cost)

    # Calculate the total cost of the pizza and toppings
    total_cost = pizza_cost + topping_cost

    # Calculate the cost per slice
    cost_per_slice = total_cost / 8

    result = cost_per_slice
    return result

print(solution())