def solution():
    # Define the number of sticks of wood each piece of furniture makes
    chair_sticks = 6
    table_sticks = 9
    stool_sticks = 2

    # Calculate the total number of sticks of wood Mary has
    total_sticks = (18 * chair_sticks) + (6 * table_sticks) + (4 * stool_sticks)

    # Calculate the number of hours Mary can keep warm
    hours = total_sticks / 5
    result = hours
    return result

print(solution())