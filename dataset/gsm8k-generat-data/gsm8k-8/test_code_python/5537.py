def solution():
    # Calculate the total number of steps logged in the first week
    week1_steps = 1000 * 7

    # Calculate the total number of steps logged in the second week
    week2_steps = (1000 + 2000) * 7

    # Calculate the total number of steps logged in the third week
    week3_steps = (1000 + 2000 + 3000) * 7

    # Calculate the total number of steps logged in the fourth week
    week4_steps = (1000 + 2000 + 3000 + 4000) * 7

    # Calculate the total number of steps logged over the 4 weeks
    total_steps = week1_steps + week2_steps + week3_steps + week4_steps

    # Calculate the difference between the total number of steps and the step goal
    goal_diff = 100000 - total_steps

    result = goal_diff
    return result

print(solution())