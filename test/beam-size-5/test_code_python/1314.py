def solution():
    num_people = 4
    num_pizzas = 7
    slices_per_pizza = 8

    # Calculate the total number of slices
    total_slices = num_pizzas * slices_per_pizza

    # Divide the total slices equally among the people
    slices_per_person = total_slices / num_people
    result = slices_per_person
    return result

print(solution())