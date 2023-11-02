def solution():
    total_students = 32  # There are 32 students in the class
    time_per_student = 5  # Each student has 5 minutes to present their project
    time_per_period = 40  # Each period is 40 minutes long

    # Calculate the total time needed for all the students to present their projects
    total_time = total_students * time_per_student

    # Calculate the number of periods needed for all the students to present their projects
    num_periods = total_time // time_per_period + 1  # We add 1 to account for any partial period
    result = num_periods
    return result

print(solution())