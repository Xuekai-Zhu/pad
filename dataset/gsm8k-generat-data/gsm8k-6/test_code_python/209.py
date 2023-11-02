def solution():
    # Calculate the total number of students
    total_students = 5 * 28  # each van carries 28 students, and there are 5 vans
    
    # Calculate the number of girls
    girls = total_students - 60  # out of the total students, 60 are boys
    
    result = girls
    return result

print(solution())