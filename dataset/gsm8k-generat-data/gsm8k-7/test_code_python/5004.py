def solution():
    num_classes = 4
    num_students_per_class = 20
    num_sheets_per_student = 5

    # Calculate the total number of students
    total_students = num_classes * num_students_per_class

    # Calculate the total number of sheets of paper needed
    total_sheets = total_students * num_sheets_per_student
    result = total_sheets
    return result

print(solution())