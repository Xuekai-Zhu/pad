def solution():
    group_1 = 25
    group_2 = 30
    total_members = 70

    # Calculate the total number of members in the first two groups
    total_group_members = group_1 + group_2

    # Calculate the number of members in the third group
    third_group = total_members - total_group_members
    result = third_group
    return result

print(solution())