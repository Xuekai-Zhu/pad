def solution():
    """There are 19 students in the 3rd grade and twice that number in the 4th grade. There are 10 boys and 19 girls in the 2nd grade. How many students are there in total?"""
    # Calculate the number of students in the 4th grade
    fourth_grade = 19 * 2

    # Calculate the total number of students
    total_students = 19 + fourth_grade + 10 + 19

    result = total_students
    return result

print(solution())