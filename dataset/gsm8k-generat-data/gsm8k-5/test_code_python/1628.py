def solution():
    # Calculate the total amount of pizza needed
    total_pizza = 1/2 + 1/3 + 1/6  # TreShawn eats 1/2, Michael eats 1/3, and LaMar eats 1/6

    # Round up to the nearest whole pizza
    pizzas_needed = math.ceil(total_pizza)

    result = pizzas_needed
    return result

print(solution())