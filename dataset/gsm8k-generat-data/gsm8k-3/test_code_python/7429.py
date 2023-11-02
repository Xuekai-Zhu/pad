def solution():
    """There are 28 students in a class. Two-sevenths of them were absent last Monday. How many students were present last Monday?"""
    # Define the number of students in the class and the portion that was absent
    total_students = 28
    absent_portion = 2/7

    # Calculate the number of absent students
    absent_students = int(absent_portion * total_students)

    # Calculate the number of present students
    present_students = total_students - absent_students

    # Display the number of present students
    result = present_students
    return result

print(solution())