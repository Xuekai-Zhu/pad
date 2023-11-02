def solution():
    """Tina's classroom has the same amount of students as Maura's. Zack's classroom has half the amount of total students between Tina and Maura's classrooms. How many students are there in total between the 3 classrooms if when Zack was sick there were 22 students in his class?"""
    zack_sick_students = 22
    total_students_tina_maura = (zack_sick_students * 2) * 2
    total_students = total_students_tina_maura + zack_sick_students
    result = total_students
    return result

print(solution())