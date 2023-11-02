def solution():
    """There are 28 students in a class. Two-sevenths of them were absent last Monday. How many students were present last Monday?"""
    # Define the total number of students and the fraction of absent students
    total_students = 28
    absent_fraction = 2/7

    # Calculate the number of absent students
    absent_students = total_students * absent_fraction

    # Calculate the number of present students
    present_students = total_students - absent_students

    # return the result
    result = present_students
    return result

print(solution())