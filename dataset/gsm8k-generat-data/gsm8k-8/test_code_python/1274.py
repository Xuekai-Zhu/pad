def solution():
    # Calculate the number of teachers who ate pizza
    pizza_teachers = int(2/3 * 30)

    # Calculate the number of staff members who ate pizza
    pizza_staff = int(4/5 * 45)

    # Calculate the total number of pizza eaters
    total_pizza_eaters = pizza_teachers + pizza_staff

    # Calculate the number of non-pizza eaters
    total_non_pizza_eaters = 30 + 45 - total_pizza_eaters
    result = total_non_pizza_eaters
    return result

print(solution())