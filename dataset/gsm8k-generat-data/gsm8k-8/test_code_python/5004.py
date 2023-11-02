def solution():
    # Define the number of classes and students
    num_classes = 4
    num_students = 20

    # Define the number of sheets of paper used per student
    num_sheets_per_student = 5

    # Calculate the total number of sheets of paper used
    total_sheets = num_classes * num_students * num_sheets_per_student
    result = total_sheets
    return result

print(solution())