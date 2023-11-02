def solution():
    # Calculate the total number of legs seen so far
    leg_count = 12 * 2 + 8 * 4 + 5 * 4

    # Calculate how many legs are needed to reach the goal
    goal_legs = 1100 - leg_count

    # Calculate the number of tarantulas needed to reach the goal
    tarantulas_needed = goal_legs // 8
    if goal_legs % 8 != 0:
        tarantulas_needed += 1

    result = tarantulas_needed
    return result

print(solution())