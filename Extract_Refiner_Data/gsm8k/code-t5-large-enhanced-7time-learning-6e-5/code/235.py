def solution():
    
    # Define the total number of students
    total_students = 1000

    # Calculate the number of students who went out through exit A
    exit_a_students = total_students * 0.3

    # Calculate the number of students who went out through exit B
    exit_b_students = (total_students - exit_a_students) * (3/5)

    # Calculate the number of students who went out through exit C
    exit_c_students = total_students - exit_a_students - exit_b_students

    # Display the number of students who went out through exit C
    result = exit_c_students
    return result

print(solution())