def solution():
    """At Esme's school, there are 30 teachers and 45 staff members. On a Monday morning, The Best Pizza Inn brought pizza for the staff and teachers as a promotion offer. If 2/3 of the teachers and 4/5 of the staff members ate Pizza, how many non-pizza eaters are at Esme's school?"""
    num_teachers = 30
    num_staff = 45
    teacher_pizza = (2/3) * num_teachers
    staff_pizza = (4/5) * num_staff
    total_pizza_eaters = teacher_pizza + staff_pizza
    total_non_eaters = num_teachers + num_staff - total_pizza_eaters
    result = total_non_eaters
    return result

print(solution())