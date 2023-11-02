def solution():
    num_boys = 9
    num_girls = 12
    group_size = 3

    # Calculate the total number of students in the class
    total_students = num_boys + num_girls

    # Calculate the number of groups that can be formed
    num_groups = total_students // group_size

    result = num_groups
    return result

print(solution())