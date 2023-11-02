def solution():
    # Calculate the total number of members in the choir
    total_members = 70

    # Calculate the total number of members in the first two groups
    first_two_groups_members = 25 + 30

    # Calculate the number of members in the third group
    third_group_members = total_members - first_two_groups_members
    result = third_group_members
    return result

print(solution())