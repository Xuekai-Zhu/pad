def solution():
    """In a class of 30 students, the teacher polls the students on their favorite subject. 1/5 of the students like Math, and 1/3 like English. 1/7 of the remaining students like Science. The rest don’t have a favorite subject. How many students don’t have a favorite subject?"""
    
    # Define the number of students in the class
    total_students = 30
    
    # Calculate the number of students who like Math
    math_students = total_students // 5
    
    # Calculate the number of students who like English
    english_students = total_students // 3
    
    # Calculate the number of remaining students
    remaining_students = total_students - math_students - english_students
    
    # Calculate the number of students who like Science
    science_students = remaining_students // 7
    
    # Calculate the number of students who don't have a favorite subject
    no_favorite_subject = total_students - math_students - english_students - science_students
    
    # Display the number of students who don't have a favorite subject
    result = no_favorite_subject
    return result

print(solution())