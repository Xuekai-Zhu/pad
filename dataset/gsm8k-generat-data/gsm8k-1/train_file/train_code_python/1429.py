def solution():
    """There are 14 girls, 11 boys, and their parents at a park. If they split into 3 equally sized playgroups, each group contains 25 people. How many parents were at the park?"""
    total_people = 14 + 11 + 2  # adding 2 for parents
    group_size = 25
    num_groups = 3
    people_per_group = group_size * num_groups
    parents_at_park = total_people - (people_per_group - 2)
    result = parents_at_park
    return result

print(solution())