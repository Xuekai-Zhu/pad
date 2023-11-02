def solution():
    """The school principal decided that she wanted every class to have an equal number of boys and girls in each first-grade classroom. There are 4 classrooms. There are 56 boys and 44 girls. How many total students are in each classroom?"""
    total_students = 56 + 44
    students_per_classroom = total_students / 4
    result = students_per_classroom
    return result

print(solution())