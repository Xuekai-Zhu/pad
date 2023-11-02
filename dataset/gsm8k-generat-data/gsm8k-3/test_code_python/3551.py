def solution():
    """Howard is taking his kindergarten class to the museum on a school trip. He splits the class equally into 3 groups and then each of the groups goes through the museum one student at a time. If the class has 18 students in total and each student takes 4 minutes to go through the museum, then how long, in minutes, does it take each group to go through the museum?"""
    # Define the number of students and time per student
    students = 18
    time_per_student = 4

    # Calculate the number of students per group
    students_per_group = students // 3

    # Calculate the total time for each group to go through the museum
    total_time = students_per_group * time_per_student

    # Display the total time per group
    result = total_time
    return result

print(solution())