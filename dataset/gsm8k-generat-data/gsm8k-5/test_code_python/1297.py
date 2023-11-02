def solution():
    total_students = 40  # There are 40 students in the class
    
    # Calculate the number of students with puppies
    students_with_puppies = total_students * 0.8
    
    # Calculate the number of students with puppies and parrots
    students_with_both = students_with_puppies * 0.25
    
    result = students_with_both
    return result

print(solution())