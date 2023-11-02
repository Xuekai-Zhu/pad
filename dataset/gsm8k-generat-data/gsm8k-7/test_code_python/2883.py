def solution():
    num_people = 6  # John and his 5 friends
    num_pizzas = 3
    num_slices_per_pizza = 8

    # Calculate the total number of slices of pizza
    total_slices = num_pizzas * num_slices_per_pizza

    # Calculate the number of slices each person ate
    slices_per_person = total_slices / num_people
    result = slices_per_person
    return result

print(solution())