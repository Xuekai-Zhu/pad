def solution():
    num_students = 18
    num_groups = 3
    time_per_student = 4

    # Calculate the number of students in each group
    students_per_group = num_students / num_groups

    # Calculate the total time for each group to go through the museum
    group_time = students_per_group * time_per_student
    result = group_time
    return result

print(solution())