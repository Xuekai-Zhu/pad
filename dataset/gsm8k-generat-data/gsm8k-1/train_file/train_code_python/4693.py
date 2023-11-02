def solution():
    """A tree had 1000 leaves before the onset of the dry season, when it sheds all its leaves. In the first week of the dry season, the tree shed 2/5 of the leaves. In the second week, it shed 40% of the remaining leaves. In the third week, the tree shed 3/4 times as many leaves as it shed on the second week. Calculate the number of leaves the tree hadn't shed by the third week."""
    initial_leaves = 1000
    week1_shed = initial_leaves * (2/5)
    week1_remaining = initial_leaves - week1_shed
    week2_shed = week1_remaining * (40/100)
    week2_remaining = week1_remaining - week2_shed
    week3_shed = week2_shed * (3/4)
    week3_remaining = week2_remaining - week3_shed
    result = week3_remaining
    
    return result

print(solution())