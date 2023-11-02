def solution():
    num_students_per_group = 6   # 5 other students plus 1
    num_sandwiches_per_student = 2
    num_groups = 5

    # Calculate the total number of students
    total_students = num_students_per_group * num_groups

    # Calculate the total number of sandwiches
    total_sandwiches = total_students * num_sandwiches_per_student

    # Calculate the total number of bread slices needed
    num_bread_slices = total_sandwiches * 2   # 2 slices per sandwich

    result = num_bread_slices
    return result

print(solution())