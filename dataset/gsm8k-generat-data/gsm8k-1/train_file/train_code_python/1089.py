def solution():
    """Beth had 150 students in her 10th-grade class. The following year 30 more students join. In her final year, 15 students left. How many students did Beth have in her class at the end of her final year?"""
    initial_students = 150
    students_joined = 30
    students_left = 15
    final_students = initial_students + students_joined - students_left
    result = final_students
    return result

print(solution())