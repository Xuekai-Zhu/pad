def solution():
    total_people = 45 + 15  # 45 people initially attend the class, and then 15 more come in later
    lollipops_per_group = 1  # The teacher gives away 1 lollipop for every 5 people in a group
    group_size = 5  # There are 5 people in each group

    # Calculate the number of groups that attended the class
    total_groups = total_people // group_size

    # Calculate the total number of lollipops the teacher gave away
    total_lollipops = total_groups * lollipops_per_group
    result = total_lollipops
    return result

print(solution())