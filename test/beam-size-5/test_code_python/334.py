def solution():
    
    # Define the total number of students and the number of students in each group
    total_students = 200
    group1_students = 2
    group2_students = total_students - group1_students
    group3_students = group2_students - 10

    # Calculate the number of students in this (smallest group)
    smallest_group_students = group3_students

    # Display the number of students in this (smallest group)
    result = smallest_group_students
    return result

print(solution())