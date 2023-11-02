def solution():
    """A choir splits into 3 groups for their performances. The first group has 25 members, and the second group has 30 members. The third group has the remaining members of the choir. If the choir overall has 70 members, how many members are in the third group?"""
    # Define the number of members in the first and second group
    first_group_members = 25
    second_group_members = 30

    # Calculate the number of members in the third group
    third_group_members = 70 - first_group_members - second_group_members

    # return the result
    result = third_group_members
    return result

print(solution())