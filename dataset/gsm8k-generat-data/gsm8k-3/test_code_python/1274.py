def solution():
    """At Esme's school, there are 30 teachers and 45 staff members. On a Monday morning, The Best Pizza Inn brought pizza for the staff and teachers as a promotion offer. If 2/3 of the teachers and 4/5 of the staff members ate Pizza, how many non-pizza eaters are at Esme's school?"""
    # Calculate the number of teachers who ate pizza
    teachers_pizza = int(2/3 * 30)

    # Calculate the number of staff members who ate pizza
    staff_pizza = int(4/5 * 45)

    # Calculate the total number of pizza eaters
    total_pizza = teachers_pizza + staff_pizza

    # Calculate the number of non-pizza eaters
    total_non_pizza = 30 + 45 - total_pizza

    # Display the number of non-pizza eaters
    result = total_non_pizza
    return result

print(solution())