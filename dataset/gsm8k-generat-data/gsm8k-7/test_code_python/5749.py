def solution():
    num_people = 12
    num_pizzas = 3
    num_slices_per_pizza = 8

    # Calculate the total number of slices
    total_slices = num_pizzas * num_slices_per_pizza

    # Divide the total number of slices by the number of people
    slices_per_person = total_slices / num_people
    result = slices_per_person
    return result

print(solution())