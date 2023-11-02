def solution():
    num_people = 10
    slices_per_person = 2
    slices_per_pizza = 4

    # Calculate the total number of slices needed
    total_slices = num_people * slices_per_person

    # Calculate the total number of pizzas needed
    total_pizzas = total_slices / slices_per_pizza
    result = total_pizzas
    return result

print(solution())