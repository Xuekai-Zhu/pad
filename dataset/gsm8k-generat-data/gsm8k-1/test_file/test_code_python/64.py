def solution():
    """There are twice as many boys as girls at Dr. Wertz's school. If there are 60 girls and 5 students to every teacher, how many teachers are there?"""
    girls = 60
    boys = 2 * girls
    total_students = girls + boys
    students_per_teacher = 5
    total_teachers = total_students // students_per_teacher
    result = total_teachers
    return result

print(solution())