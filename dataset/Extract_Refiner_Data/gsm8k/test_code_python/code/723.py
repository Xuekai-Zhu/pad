def solution():
    
    # Define the number of windows in each type of car
    STUDENT_WINDOWS = 4
    TEACHER_WINDOWS = 2

    # Define the number of students' and teachers' cars
    students_cars = 64
    teachers_cars = 32

    # Calculate the number of windows smashed for students' and teachers' cars
    students_windows = students_cars * STUDENT_WINDOWS / 4
    teachers_windows = teachers_cars * TEACHER_WINDOWS * 0.75

    # Calculate the total number of windows smashed
    total_windows = students_windows + teachers_windows

    # Display the total number of windows smashed
    result = total_windows
    return result

print(solution())