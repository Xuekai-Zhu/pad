def solution():
    # Define the total number of students
    total_students = 325

    # Calculate the number of students with glasses
    glasses_students = 0.4 * total_students

    # Calculate the number of students without glasses
    no_glasses_students = total_students - glasses_students
    result = no_glasses_students
    return result

print(solution())