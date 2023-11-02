def solution():
    cost_of_pizza = 10.00  # The cost of a large pizza is $10.00
    slices_per_pizza = 8  # A large pizza is cut into 8 slices
    cost_of_first_topping = 2.00  # The first topping costs $2.00
    cost_of_second_topping = 1.00  # The second topping costs $1.00
    cost_of_rest_of_toppings = 0.50  # The rest of the toppings cost $0.50

    # Calculate the total cost of the pizza with all toppings
    total_cost_of_toppings = cost_of_first_topping + (2 * cost_of_second_topping) + (4 * cost_of_rest_of_toppings)
    total_cost_of_pizza = cost_of_pizza + total_cost_of_toppings

    # Calculate the cost per slice of the pizza
    cost_per_slice = total_cost_of_pizza / slices_per_pizza
    result = cost_per_slice
    return result

print(solution())