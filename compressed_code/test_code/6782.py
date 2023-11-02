def solution():
    
    num_teachers = 30
    num_staff = 45
    teacher_pizza = (2/3) * num_teachers
    staff_pizza = (4/5) * num_staff
    total_pizza_eaters = teacher_pizza + staff_pizza
    total_non_eaters = num_teachers + num_staff - total_pizza_eaters
    result = total_non_eaters
    return result

print(solution())