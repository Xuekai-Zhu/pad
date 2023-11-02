def solution():
    # Define the number of students in each grade
    k_students = 26
    f_students = 19
    s_students = 20
    t_students = 25

    # Calculate the total number of lice checks
    total_checks = k_students + f_students + s_students + t_students

    # Calculate the total time in minutes
    total_time_min = total_checks * 2

    # Calculate the total time in hours
    total_time_hours = total_time_min / 60

    result = total_time_hours
    return result

print(solution())