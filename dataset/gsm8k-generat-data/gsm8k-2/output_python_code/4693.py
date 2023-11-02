def solution():
    """A tree had 1000 leaves before the onset of the dry season, when it sheds all its leaves. In the first week of the dry season, the tree shed 2/5 of the leaves. In the second week, it shed 40% of the remaining leaves. In the third week, the tree shed 3/4 times as many leaves as it shed on the second week. Calculate the number of leaves the tree hadn't shed by the third week."""
    start_leaves = 1000
    first_week_shed = start_leaves * (2/5)
    remaining_leaves = start_leaves - first_week_shed
    second_week_shed = remaining_leaves * 0.4
    remaining_leaves = remaining_leaves - second_week_shed
    third_week_shed = second_week_shed * (3/4)
    remaining_leaves = remaining_leaves - third_week_shed
    result = remaining_leaves
    return result

print(solution())