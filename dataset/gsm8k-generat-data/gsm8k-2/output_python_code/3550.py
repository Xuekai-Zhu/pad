def solution():
    """Howard is taking his kindergarten class to the museum on a school trip. He splits the class equally into 3 groups and then each of the groups goes through the museum one student at a time. If the class has 18 students in total and each student takes 4 minutes to go through the museum, then how long, in minutes, does it take each group to go through the museum?"""
    total_students = 18
    group_size = total_students / 3
    time_per_student = 4
    time_per_group = group_size * time_per_student
    result = time_per_group
    return result

print(solution())