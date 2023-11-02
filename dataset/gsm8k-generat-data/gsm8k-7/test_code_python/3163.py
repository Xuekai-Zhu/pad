def solution():
    num_slices_per_pizza = 18
    num_pizzas = 6
    leftover_cheese = 8
    leftover_onion = 4

    # Calculate the total number of cheese slices ordered
    total_cheese = (num_pizzas * num_slices_per_pizza) - leftover_cheese

    # Calculate the total number of onion slices ordered
    total_onion = (num_pizzas * num_slices_per_pizza) - leftover_onion

    # Calculate the number of students in the class
    num_students = total_cheese // 2

    result = num_students
    return result

print(solution())