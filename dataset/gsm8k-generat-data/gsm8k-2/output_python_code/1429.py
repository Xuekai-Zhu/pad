def solution():
    """There are 14 girls, 11 boys, and their parents at a park. If they split into 3 equally sized playgroups, each group contains 25 people. How many parents were at the park?"""
    total_people = 14 + 11 + 2 * (14 + 11) # total number of people (girls + boys + parents)
    group_size = 25
    num_groups = 3
    parent_count = (total_people - num_groups * group_size) / 2 # each group has equal number of parents
    result = parent_count
    return result

print(solution())