def solution():
    """Evergreen Elementary school has 100 students in Grades 4, 5, and 6. There are 30 students in Grade 4 and 35 students in Grade 5. How many students are in Grade 6?"""
    total_students = 100
    grade_4_students = 30
    grade_5_students = 35
    grade_6_students = total_students - grade_4_students - grade_5_students
    result = grade_6_students
    return result

print(solution())