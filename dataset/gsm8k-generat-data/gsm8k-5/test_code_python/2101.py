def solution():
    people = 10  # Brenda and 9 of her friends
    slices_per_person = 2  # Each person will eat 2 slices
    slices_per_pizza = 4  # Each pizza has 4 slices

    # Calculate the total number of slices needed
    total_slices_needed = people * slices_per_person

    # Calculate the number of pizzas needed
    pizzas_needed = total_slices_needed / slices_per_pizza
    result = pizzas_needed
    return result

# They should order 5 pizzas.

print(solution())