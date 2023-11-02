def solution():
    pizzas = 3  # John and his friends ordered 3 pizzas
    slices_per_pizza = 8  # Each pizza had 8 slices
    total_slices = pizzas * slices_per_pizza  # Total number of slices

    # Divide the slices evenly among 6 people (John and his 5 friends)
    slices_per_person = total_slices / 6
    result = slices_per_person
    return result

print(solution())