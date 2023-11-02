def solution():
    """Miss Davis gave 15 popsicle sticks to each of the 10 groups in her class. How many sticks does she have left if she had 170 popsicle sticks?"""
    sticks_per_group = 15
    num_groups = 10
    total_sticks = sticks_per_group * num_groups
    sticks_left = 170 - total_sticks
    result = sticks_left
    return result

print(solution())