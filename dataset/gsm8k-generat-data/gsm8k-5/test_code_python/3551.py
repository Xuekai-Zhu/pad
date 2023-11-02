def solution():
    total_students = 18  # There are 18 students in the class
    group_size = total_students // 3  # The class is split into 3 equal groups
    time_per_student = 4  # Each student takes 4 minutes to go through the museum

    # Calculate the time each group takes to go through the museum
    group_time = group_size * time_per_student

    result = group_time
    return result

print(solution())