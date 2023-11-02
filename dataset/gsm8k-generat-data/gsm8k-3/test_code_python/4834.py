def solution():
    """James wants to build a ladder to climb a very tall tree.  Each rung of the ladder is 18 inches long and they are 6 inches apart.  If he needs to climb 50 feet how many feet of wood will he need for the rungs?"""
    # Define the length of each rung in feet
    RUNG_LENGTH_FEET = 1.5

    # Define the distance between each rung in feet
    RUNG_DISTANCE_FEET = 0.5

    # Define the height of the tree in feet
    TREE_HEIGHT_FEET = 50

    # Calculate the number of rungs needed
    total_rungs = TREE_HEIGHT_FEET / RUNG_DISTANCE_FEET

    # Calculate the length of wood needed for all the rungs
    total_rung_length = total_rungs * RUNG_LENGTH_FEET

    # Display the length of wood needed
    result = total_rung_length
    return result

print(solution())