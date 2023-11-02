def solution():
    # Calculate the total amount of pizza needed
    total_pizza = 0.5 + (1/3) + (1/6)

    # Round up to the nearest whole pizza
    pizzas_needed = math.ceil(total_pizza)

    result = pizzas_needed
    return result

print(solution())