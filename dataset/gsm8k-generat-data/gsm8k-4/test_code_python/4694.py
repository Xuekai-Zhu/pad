def solution():
    """A tree had 1000 leaves before the onset of the dry season, when it sheds all its leaves. In the first week of the dry season, the tree shed 2/5 of the leaves. In the second week, it shed 40% of the remaining leaves. In the third week, the tree shed 3/4 times as many leaves as it shed on the second week. Calculate the number of leaves the tree hadn't shed by the third week."""
    # Define the initial number of leaves
    initial_leaves = 1000

    # Calculate the number of leaves shed in the first week
    week1_shed = initial_leaves * (2/5)

    # Calculate the number of leaves remaining after the first week
    week1_remaining = initial_leaves - week1_shed

    # Calculate the number of leaves shed in the second week
    week2_shed = week1_remaining * (40/100)

    # Calculate the number of leaves remaining after the second week
    week2_remaining = week1_remaining - week2_shed

    # Calculate the number of leaves shed in the third week
    week3_shed = week2_shed * (3/4)

    # Calculate the number of leaves remaining after the third week
    leaves_remaining = week2_remaining - week3_shed

    # Return the result
    result = leaves_remaining
    return result

print(solution())