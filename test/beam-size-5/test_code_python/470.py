def solution():
    
    # Define the total number of students
    total_students = 20

    # Calculate the number of students with desktop computers
    desktop_computers = total_students * 0.75

    # Calculate the number of students at the grade level
    grade_level_students = total_students - desktop_computers

    # Display the number of students at the grade level
    result = grade_level_students
    return result

print(solution())