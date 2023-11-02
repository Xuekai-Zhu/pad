def solution():
    """There are 9 boys and 12 girls in a class. The teacher needs to create groups with three members for their class activity. How many groups are formed?"""
    total_students = 9 + 12
    group_size = 3
    num_groups = total_students // group_size
    result = num_groups
    return result

print(solution())