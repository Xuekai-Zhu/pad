def solution():
    """Miss Davis gave 15 popsicle sticks to each of the 10 groups in her class. How many sticks does she have left if she had 170 popsicle sticks?"""
    # Define the number of groups and number of sticks per group
    NUM_GROUPS = 10
    STICKS_PER_GROUP = 15

    # Calculate the total number of sticks given out
    total_sticks_given = NUM_GROUPS * STICKS_PER_GROUP

    # Calculate the number of sticks remaining
    sticks_remaining = 170 - total_sticks_given

    # Display the number of sticks remaining
    result = sticks_remaining
    return result

print(solution())