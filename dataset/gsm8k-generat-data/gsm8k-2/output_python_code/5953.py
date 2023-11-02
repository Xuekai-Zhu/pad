def solution():
    """Tina's classroom has the same amount of students as Maura's. Zack's classroom has half the amount of total students between Tina and Maura's classrooms. How many students are there in total between the 3 classrooms if when Zack was sick there were 22 students in his class?"""
    zack_sick = 22
    total_students = zack_sick * 2  # double the number of students in Zack's class
    tina_maura = total_students // 2  # divide total students by 2 to get the sum of Tina and Maura's classrooms
    total_students += tina_maura  # add Tina and Maura's classroom to total students

    result = total_students
    return result

print(solution())