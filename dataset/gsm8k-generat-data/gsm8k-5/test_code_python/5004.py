def solution():
    num_classes = 4  # Miss Adamson has 4 classes
    num_students = 20  # Each class has 20 students
    num_sheets_per_student = 5  # Miss Adamson uses 5 sheets of paper per student

    # Calculate the total number of sheets of paper Miss Adamson will use
    total_sheets = num_classes * num_students * num_sheets_per_student
    result = total_sheets
    return result

print(solution())