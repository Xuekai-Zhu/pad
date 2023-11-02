def solution():
    total_members = 70  # The choir has 70 members in total
    first_group_members = 25  # The first group has 25 members
    second_group_members = 30  # The second group has 30 members

    # Calculate the number of members in the third group
    third_group_members = total_members - first_group_members - second_group_members
    result = third_group_members
    return result

print(solution())