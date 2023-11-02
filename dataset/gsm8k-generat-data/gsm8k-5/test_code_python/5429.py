def solution():
    groups = 10  # Miss Davis has given popsicle sticks to 10 groups
    sticks_per_group = 15  # Each group has been given 15 popsicle sticks
    total_sticks = 170  # Miss Davis had 170 popsicle sticks to begin with

    # Calculate the total number of popsicle sticks given to the groups
    sticks_given = groups * sticks_per_group

    # Calculate the number of popsicle sticks Miss Davis has left
    sticks_left = total_sticks - sticks_given
    result = sticks_left
    return result

print(solution())