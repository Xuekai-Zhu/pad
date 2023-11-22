def solution():
    
    # Define the total number of students and the number of groups required
    total_students = 50
    groups_required = 12

    # Calculate the number of students in each group
    students_per_group = total_students / 6

    # Calculate the number of additional groups required
    additional_groups_required = (groups_required - 1) // students_per_group

    # return the result
    result = additional_groups_required
    return result

print(solution())