def solution():
    num_teachers = 30
    num_staff = 45

    # Calculate the number of teachers that ate pizza
    num_teachers_pizza = int(num_teachers * 2 / 3)

    # Calculate the number of staff members that ate pizza
    num_staff_pizza = int(num_staff * 4 / 5)

    # Calculate the total number of pizza eaters
    total_pizza_eaters = num_teachers_pizza + num_staff_pizza

    # Calculate the number of non-pizza eaters
    num_non_pizza_eaters = num_teachers + num_staff - total_pizza_eaters

    result = num_non_pizza_eaters
    return result

print(solution())