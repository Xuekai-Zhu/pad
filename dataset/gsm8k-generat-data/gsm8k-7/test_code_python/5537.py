def solution():
    step_goal = 100000

    # Calculate the total steps logged in the first week
    total_steps_week_1 = 7 * 1000

    # Calculate the total steps logged in the second week
    total_steps_week_2 = (7 + 6 + 5 + 4 + 3 + 2 + 1) * 1000

    # Calculate the total steps logged in the third week
    total_steps_week_3 = (7 + 8 + 9 + 10 + 11 + 12 + 13) * 1000

    # Calculate the total steps logged in the fourth week
    total_steps_week_4 = (7 + 14 + 21 + 28 + 35 + 42 + 49) * 1000

    # Calculate the total steps logged over the 4 weeks
    total_steps = total_steps_week_1 + total_steps_week_2 + total_steps_week_3 + total_steps_week_4

    # Calculate how far away from the step goal Cody is
    steps_away_from_goal = step_goal - total_steps
    result = steps_away_from_goal
    return result

print(solution())