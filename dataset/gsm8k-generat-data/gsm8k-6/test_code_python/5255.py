def solution():
    # Calculate the number of slices in each pizza
    slices_per_pizza = 16 / 2  # both pizzas have 16 slices in total

    # Calculate the number of slices of cheese pizza each person gets
    slices_per_person_cheese = (slices_per_pizza - 1) / 3  # one slice of pepperoni left, so only 3 people have cheese pizza

    # Calculate the number of slices of pepperoni pizza each person gets
    slices_per_person_pepperoni = (slices_per_pizza + 1) / 1  # one friend eats only pepperoni pizza

    # Calculate the total number of slices each person gets
    total_slices_per_person = slices_per_person_cheese + slices_per_person_pepperoni

    result = total_slices_per_person
    return result

print(solution())