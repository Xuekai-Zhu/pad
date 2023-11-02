def solution():
    num_girls = 14
    num_boys = 11
    total_children = num_girls + num_boys
    num_playgroups = 3
    group_size = 25

    # Calculate the total number of people at the park
    total_people = total_children + num_playgroups * group_size

    # Calculate the number of parents at the park
    num_parents = total_people - total_children
    result = num_parents
    return result

print(solution())