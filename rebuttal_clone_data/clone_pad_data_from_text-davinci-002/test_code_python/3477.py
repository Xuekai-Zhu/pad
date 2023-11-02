def solution():
    math_students_volunteering = 5
    number_of_math_classes = 6
    total_math_students = math_students_volunteering * number_of_math_classes
    teachers_volunteering = 13
    total_volunteers = total_math_students + teachers_volunteering
    volunteers_ needed = 50 - total_volunteers
    result = volunteers_needed
    return result

print(solution())