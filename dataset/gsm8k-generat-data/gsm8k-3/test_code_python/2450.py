def solution():
    """Jamie is a firefighter. One day an emergency call comes in from Mrs. Thompson, an elderly woman whose cat can't get down a 20-foot tree. The last time Jamie rescued a cat, he got it down from a 6-foot tree and had to climb 12 rungs of his ladder. How many rungs does he have to climb this time to get the cat down from the tree?"""
    # Define the height of the previous tree and the corresponding number of ladder rungs used
    PREV_TREE_HEIGHT = 6
    PREV_RUNGS_USED = 12

    # Define the height of the current tree
    TREE_HEIGHT = 20

    # Calculate the ratio between tree heights and ladder rungs used
    ratio = PREV_RUNGS_USED / PREV_TREE_HEIGHT

    # Calculate the number of ladder rungs needed for the current tree height
    rungs_needed = ratio * TREE_HEIGHT

    # Display the number of ladder rungs needed
    result = rungs_needed
    return result

print(solution())