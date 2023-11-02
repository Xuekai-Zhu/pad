def solution():
    """Howard is taking his kindergarten class to the museum on a school trip. He splits the class equally into 3 groups and then each of the groups goes through the museum one student at a time. If the class has 18 students in total and each student takes 4 minutes to go through the museum, then how long, in minutes, does it take each group to go through the museum?"""
    # Define the number of students in the class and the time to go through the museum
    total_students = 18
    time_per_student = 4

    # Calculate the number of students in each group
    students_per_group = total_students // 3

    # Calculate the time for each group to go through the museum
    group_time = students_per_group * time_per_student

    result = group_time
    return result

print(solution())