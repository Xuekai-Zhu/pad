def solution():
    # Calculate the total number of sticks given to the groups
    total_given_sticks = 15 * 10  # Miss Davis gave 15 sticks to each of the 10 groups
    # Calculate the number of sticks she has left
    sticks_left = 170 - total_given_sticks
    result = sticks_left
    return result

print(solution())