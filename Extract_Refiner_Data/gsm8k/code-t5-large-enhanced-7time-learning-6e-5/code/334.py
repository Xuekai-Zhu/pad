def solution():
    
    # Define the total number of students
    total_students = 200

    # Calculate the number of students in the first group
    group1_students = total_students / 2

    # Calculate the number of students in the second group
    group2_students = group1_students / 2

    # Calculate the number of students in the third group
    group3_students = group2_students - 10

    # Calculate the number of students in the smallest group
    smallest_group_students = group3_students

    # Display the number of students in the smallest group
    result = smallest_group_students
    return result

print(solution())