def solution():
    num_people = 18
    slices_per_person = 3
    slices_per_pizza = 9

    # Calculate the total number of slices needed
    total_slices = num_people * slices_per_person

    # Calculate the number of pizzas needed
    num_pizzas = total_slices // slices_per_pizza
    if total_slices % slices_per_pizza != 0:
      num_pizzas += 1

    result = num_pizzas
    return result

print(solution())