def solution():
    """A class of 200 students is split into 3 groups such that 2 of them are equal in number and the last one (which is the smallest) is 10 less than each of the other groups. How many students are in this (smallest) group?"""
    total_students = 200
    small_group_difference = 10
    large_groups_total = total_students - small_group_difference
    equal_groups_total = large_groups_total / 2
    small_group_total = equal_groups_total - small_group_difference
    result = small_group_total
    return result

print(solution())