def solution():
    """Miss Adamson has four classes with 20 students each. She makes a study guide for her class and uses 5 sheets of paper per student. How many sheets of paper will she use for all of her students?"""
    # Define the number of classes and students per class
    CLASSES = 4
    STUDENTS_PER_CLASS = 20

    # Define the number of sheets of paper used per student
    SHEETS_PER_STUDENT = 5

    # Calculate the total number of sheets of paper needed
    total_sheets = CLASSES * STUDENTS_PER_CLASS * SHEETS_PER_STUDENT

    # Display the total number of sheets of paper needed
    result = total_sheets
    return result

print(solution())