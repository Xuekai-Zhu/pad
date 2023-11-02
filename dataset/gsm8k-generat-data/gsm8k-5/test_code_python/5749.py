def solution():
    num_people = 12  # There are 12 coworkers
    num_pizzas = 3  # They ordered 3 pizzas
    slices_per_pizza = 8  # Each pizza is cut into 8 slices

    # Calculate the total number of slices
    total_slices = num_pizzas * slices_per_pizza

    # Calculate the number of slices each person will get
    slices_per_person = total_slices / num_people
    result = slices_per_person
    return result

print(solution())