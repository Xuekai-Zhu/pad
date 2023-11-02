def solution():
    """A choir splits into 3 groups for their performances. The first group has 25 members, and the second group has 30 members. The third group has the remaining members of the choir. If the choir overall has 70 members, how many members are in the third group?"""
    # Define the size of the first two groups
    group1_size = 25
    group2_size = 30

    # Calculate the size of the third group
    group3_size = 70 - group1_size - group2_size

    # Display the size of the third group
    result = group3_size
    return result

print(solution())