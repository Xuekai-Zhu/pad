def solution():
    total_students = 24
    group_one = 5
    group_two = 8
    group_three = 7

    # Calculate the number of students in the first three groups
    total_group_students = group_one + group_two + group_three

    # Calculate the number of students in the fourth group
    group_four = total_students - total_group_students
    result = group_four
    return result

print(solution())