def solution():
    pizza_cost = 10.0
    num_slices = 8
    topping1_cost = 2.0
    topping2_cost = 1.0
    topping_rest_cost = 0.5
    num_toppings = 6

    # Calculate the total cost of toppings
    total_topping_cost = (topping1_cost + (2*topping2_cost) + ((num_toppings-3)*topping_rest_cost))

    # Calculate the total cost of pizza with toppings
    total_cost = pizza_cost + total_topping_cost

    # Calculate the cost per slice
    cost_per_slice = total_cost / num_slices
    result = cost_per_slice
    return result

print(solution())