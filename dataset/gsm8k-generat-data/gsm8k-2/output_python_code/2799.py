def solution():
    """There are 20 boys and 11 girls in the second grade and twice that number in the third grade. How many students are in grades 2 and 3?"""
    second_grade_students = 20 + 11
    third_grade_students = 2 * second_grade_students
    total_students = second_grade_students + third_grade_students
    result = total_students
    return result

print(solution())