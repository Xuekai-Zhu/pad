def solution():
    """There are 19 students in the 3rd grade and twice that number in the 4th grade.
    There are 10 boys and 19 girls in the 2nd grade. How many students are there in total?"""
    third_grade = 19
    fourth_grade = third_grade * 2
    second_grade = 10 + 19
    total_students = third_grade + fourth_grade + second_grade
    result = total_students
    return result

print(solution())