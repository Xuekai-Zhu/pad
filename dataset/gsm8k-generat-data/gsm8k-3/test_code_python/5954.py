def solution():
    """Tina's classroom has the same amount of students as Maura's. Zack's classroom has half the amount of total students between Tina and Maura's classrooms. How many students are there in total between the 3 classrooms if when Zack was sick there were 22 students in his class?"""
    # Let x be the number of students in Tina's and Maura's classrooms
    x = 22*2  # since Zack's class has half the total students between Tina and Maura's classrooms
    total_students = x + 22*3  # add number of students in Zack's class to x to get total
    result = total_students
    return result

print(solution())