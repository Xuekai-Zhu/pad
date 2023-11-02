def solution():
    """Texas Integrated School has 15 classes and has 20 students per class.  They added five more classes, how many students will they have now?"""
    
    # Define the initial number of classes and students per class
    initial_classes = 15
    initial_students_per_class = 20
    
    # Define the number of classes added
    classes_added = 5
    
    # Calculate the total number of classes
    total_classes = initial_classes + classes_added
    
    # Calculate the total number of students
    total_students = total_classes * initial_students_per_class
    
    # Return the total number of students
    result = total_students
    return result

print(solution())