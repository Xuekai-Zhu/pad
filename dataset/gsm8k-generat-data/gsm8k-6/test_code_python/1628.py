def solution():
    # Calculate the total fraction of pizza needed
    total_fraction = 1/2 + 1/3 + 1/6  # TreShawn eats 1/2, Michael eats 1/3, LaMar eats 1/6
    # Round up to the nearest whole pizza
    pizzas_needed = math.ceil(total_fraction)
    result = pizzas_needed
    return result

print(solution())