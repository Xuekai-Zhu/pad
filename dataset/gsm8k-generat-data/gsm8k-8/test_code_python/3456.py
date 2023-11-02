def solution():
    # Calculate the total number of students in the first three groups
    total_students_in_first_three_groups = 5 + 8 + 7

    # Calculate the number of students in the fourth group
    students_in_fourth_group = 24 - total_students_in_first_three_groups

    result = students_in_fourth_group
    return result

print(solution())