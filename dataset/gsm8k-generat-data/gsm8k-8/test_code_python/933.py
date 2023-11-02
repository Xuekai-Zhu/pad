def solution():
    # Define the number of steps in each staircase
    staircase1 steps = 20
    staircase2_steps = 2 * staircase1_steps
    staircase3_steps = staircase2_steps - 10

    # Calculate the total number of steps climbed
    total_steps = staircase1_steps + staircase2_steps + staircase3_steps

    # Calculate the total distance climbed in feet
    total_distance = total_steps * 0.5
    result = total_distance
    return result

print(solution())