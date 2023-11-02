def solution():
    """There are 28 students in a class. Two-sevenths of them were absent last Monday. How many students were present last Monday?"""
    total_students = 28
    absent_students = total_students * (2/7)
    present_students = total_students - absent_students
    result = present_students
    return result

print(solution())