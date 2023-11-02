def solution():
    slices_per_person = 3  # Each person gets 3 slices
    slices_per_pizza = 9  # Each pizza has 9 slices
    num_people = 18  # There are 18 people in the group

    # Calculate the total number of slices needed
    total_slices = slices_per_person * num_people

    # Calculate the number of pizzas needed
    pizzas_needed = total_slices / slices_per_pizza
    result = pizzas_needed
    return result

print(solution())