def solution():
    """A tree had 1000 leaves before the onset of the dry season, when it sheds all its leaves. In the first week of the dry season, the tree shed 2/5 of the leaves. In the second week, it shed 40% of the remaining leaves. In the third week, the tree shed 3/4 times as many leaves as it shed on the second week. Calculate the number of leaves the tree hadn't shed by the third week."""
    # Define the initial number of leaves
    initial_leaves = 1000

    # Calculate the number of leaves shed in the first week
    leaves_shed_1 = int(2/5 * initial_leaves)
    remaining_leaves_1 = initial_leaves - leaves_shed_1

    # Calculate the number of leaves shed in the second week
    leaves_shed_2 = int(0.4 * remaining_leaves_1)
    remaining_leaves_2 = remaining_leaves_1 - leaves_shed_2

    # Calculate the number of leaves shed in the third week
    leaves_shed_3 = int(3/4 * leaves_shed_2)
    remaining_leaves_3 = remaining_leaves_2 - leaves_shed_3

    # Display the number of leaves that haven't been shed by the third week
    result = remaining_leaves_3
    return result

print(solution())