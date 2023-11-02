def solution():
    """At Esme's school, there are 30 teachers and 45 staff members. On a Monday morning, The Best Pizza Inn brought pizza for the staff and teachers as a promotion offer. If 2/3 of the teachers and 4/5 of the staff members ate Pizza, how many non-pizza eaters are at Esme's school?"""
    total_people = 30 + 45
    pizza_eaters = (2/3) * 30 + (4/5) * 45
    non_pizza_eaters = total_people - pizza_eaters
    result = non_pizza_eaters
    return result

print(solution())