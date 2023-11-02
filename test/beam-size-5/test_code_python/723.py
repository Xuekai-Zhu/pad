def solution():
    
    # Define the number of students' and teachers' cars
    num_students = 64
    num_teachers = 32

    # Calculate the number of students' and teachers' windows
    num_students_windows = num_students / 4
    num_teachers_windows = num_teachers * (3/4)

    # Calculate the total number of windows smashed
    total_windows_smashed = (num_students_windows * 4) + (num_teachers_windows * 2)

    # return the result
    result = total_windows_smashed
    return result

print(solution())