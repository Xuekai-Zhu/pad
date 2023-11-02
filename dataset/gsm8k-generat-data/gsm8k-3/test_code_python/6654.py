def solution():
    """John buys 2 packs of index cards for all his students.  He has 6 classes and 30 students in each class. How many packs did he buy?"""
    # Define the number of classes and students per class
    NUM_CLASSES = 6
    STUDENTS_PER_CLASS = 30

    # Calculate the total number of students
    total_students = NUM_CLASSES * STUDENTS_PER_CLASS

    # Calculate the total number of packs needed
    total_packs = 2 * total_students

    # Display the total number of packs bought
    result = total_packs
    return result

print(solution())