def solution():
    """Miss Davis gave 15 popsicle sticks to each of the 10 groups in her class. How many sticks does she have left if she had 170 popsicle sticks?"""
    # Define the number of groups and popsicle sticks
    num_groups = 10
    total_sticks = 170

    # Calculate the number of sticks given out to all the groups
    sticks_given = num_groups * 15

    # Calculate the number of sticks left with Miss Davis
    sticks_left = total_sticks - sticks_given

    # return the result
    result = sticks_left
    return result

print(solution())