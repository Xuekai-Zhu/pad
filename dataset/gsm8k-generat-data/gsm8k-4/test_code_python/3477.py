def solution():
    """Mr. Johnson is organizing the school Christmas play and needs 50 volunteers to help with decorating the auditorium. 5 students from each of the school’s 6 math classes have volunteered to help. 13 teachers have also volunteered to help. How many more volunteers will Mr. Johnson need?"""
    # Define the number of students in each math class
    students_per_class = 5

    # Define the number of math classes
    num_classes = 6

    # Calculate the number of student volunteers
    student_volunteers = students_per_class * num_classes

    # Define the number of teacher volunteers
    teacher_volunteers = 13

    # Calculate the total number of volunteers
    total_volunteers = student_volunteers + teacher_volunteers

    # Define the number of volunteers Mr. Johnson needs
    volunteers_needed = 50

    # Calculate the number of more volunteers Mr. Johnson needs
    more_volunteers_needed = volunteers_needed - total_volunteers

    # Return the result
    result = more_volunteers_needed
    return result

print(solution())