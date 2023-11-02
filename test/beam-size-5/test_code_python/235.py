def solution():
    
    # Define the total number of students and the number of entrances
    total_students = 1000
    num_entrances = 3

    # Calculate the number of students who went out through exit A
    num_students_A = int(total_students * 0.3)

    # Calculate the number of students who went out through exit B
    num_students_B = int(total_students - num_students_A)

    # Calculate the number of students who went out through exit C
    num_students_C = total_students - num_students_A - num_students_B

    # Display the number of students who went out through exit C
    result = num_students_C
    return result

print(solution())