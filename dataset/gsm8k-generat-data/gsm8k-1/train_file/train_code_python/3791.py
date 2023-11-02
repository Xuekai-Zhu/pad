def solution():
    """A choir splits into 3 groups for their performances. The first group has 25 members, and the second group has 30 members. The third group has the remaining members of the choir. If the choir overall has 70 members, how many members are in the third group?"""
    total_members = 70
    first_group = 25
    second_group = 30
    third_group = total_members - first_group - second_group
    result = third_group
    return result

print(solution())