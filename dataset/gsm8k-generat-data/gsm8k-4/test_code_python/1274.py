def solution():
    """At Esme's school, there are 30 teachers and 45 staff members. On a Monday morning, The Best Pizza Inn brought pizza for the staff and teachers as a promotion offer. If 2/3 of the teachers and 4/5 of the staff members ate Pizza, how many non-pizza eaters are at Esme's school?"""
    # Define the total number of teachers and staff
    total_personnel = 30 + 45

    # Calculate the number of teachers who ate pizza
    pizza_eating_teachers = 30 * 2/3

    # Calculate the number of staff members who ate pizza
    pizza_eating_staff = 45 * 4/5

    # Calculate the total number of pizza eaters
    total_pizza_eaters = pizza_eating_teachers + pizza_eating_staff

    # Calculate the number of non-pizza eaters
    non_pizza_eaters = total_personnel - total_pizza_eaters

    # return the result
    result = non_pizza_eaters
    return result

print(solution())