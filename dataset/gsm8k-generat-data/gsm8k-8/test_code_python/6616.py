def solution():
    # Define the total number of students
    total_students = 50

    # Define the number of students transferred
    transferred_students = 2

    # Calculate the number of students in each section before the transfer
    section_students = (total_students - transferred_students) / 2
    result = section_students
    return result

print(solution())