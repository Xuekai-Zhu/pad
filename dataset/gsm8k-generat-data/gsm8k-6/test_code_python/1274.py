def solution():
    # Calculate the number of teachers who ate pizza
    teachers_pizza = (2/3) * 30

    # Calculate the number of staff members who ate pizza
    staff_pizza = (4/5) * 45

    # Calculate the total number of pizza eaters
    total_pizza_eaters = teachers_pizza + staff_pizza

    # Calculate the number of non-pizza eaters
    non_pizza_eaters = 30 + 45 - total_pizza_eaters

    result = non_pizza_eaters
    return result

print(solution())