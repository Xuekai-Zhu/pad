def solution():
    """There are 20 boys and 11 girls in the second grade and twice that number in the third grade. How many students are in grades 2 and 3?"""
    # Define the number of students in the second grade
    grade_2 = 20 + 11

    # Define the number of students in the third grade
    grade_3 = grade_2 * 2

    # Calculate the total number of students in grades 2 and 3
    total_students = grade_2 + grade_3

    # return the result
    result = total_students
    return result

print(solution())