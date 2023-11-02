def solution():
    """Miss Adamson has four classes with 20 students each. She makes a study guide for her class and uses 5 sheets of paper per student. How many sheets of paper will she use for all of her students?"""
    num_classes = 4
    num_students_per_class = 20
    sheets_per_student = 5
    total_sheets = num_classes * num_students_per_class * sheets_per_student
    result = total_sheets
    return result

print(solution())