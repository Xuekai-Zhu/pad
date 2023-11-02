def solution():
    total_leaves = 1000  # The tree had 1000 leaves before the onset of the dry season
    leaves_shed_first_week = (2/5) * total_leaves  # The tree shed 2/5 of its leaves in the first week
    leaves_remaining = total_leaves - leaves_shed_first_week  # The number of leaves remaining after the first week
    leaves_shed_second_week = 0.4 * leaves_remaining  # The tree shed 40% of the remaining leaves in the second week
    leaves_remaining = leaves_remaining - leaves_shed_second_week  # The number of leaves remaining after the second week
    leaves_shed_third_week = (3/4) * leaves_shed_second_week  # The tree shed 3/4 of the leaves it shed in the second week in the third week
    leaves_remaining = leaves_remaining - leaves_shed_third_week  # The number of leaves remaining after the third week
    result = leaves_remaining
    return result

print(solution())