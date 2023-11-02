def solution():
    """Miss Adamson has four classes with 20 students each. She makes a study guide for her class and uses 5 sheets of paper per student. How many sheets of paper will she use for all of her students?"""
    num_of_classes = 4
    num_of_students = 20
    num_of_sheets_per_student = 5
    total_num_of_sheets = num_of_classes * num_of_students * num_of_sheets_per_student
    result = total_num_of_sheets
    return result

print(solution())