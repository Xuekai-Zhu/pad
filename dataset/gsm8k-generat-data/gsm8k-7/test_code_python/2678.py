def solution():
    num_pizza_per_day = 3
    num_days = 72
    num_slices_per_pizza = 8

    # Calculate the total number of slices of pizza Nunzio eats in 72 days
    total_slices = num_pizza_per_day * num_days * num_slices_per_pizza

    # Calculate the total number of pizzas Nunzio eats in 72 days
    total_pizzas = total_slices / num_slices_per_pizza
    result = total_pizzas
    return result

print(solution())