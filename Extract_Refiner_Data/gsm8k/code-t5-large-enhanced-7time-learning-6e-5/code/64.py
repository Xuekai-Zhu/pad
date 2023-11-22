def solution():
    
    # Define the number of girls and boys
    girls = 60
    boys = girls * 2

    # Calculate the total number of students
    total_students = girls + boys

    # Calculate the number of teachers
    teachers = total_students // 5

    # Display the number of teachers
    result = teachers
    return result

print(solution())