def solution():
    """There are 20 boys and 11 girls in the second grade and twice that number in the third grade. How many students are in grades 2 and 3?"""
    grade_two_students = 20 + 11
    grade_three_students = 2 * grade_two_students
    total_students = grade_two_students + grade_three_students
    result = total_students
    return result

print(solution())