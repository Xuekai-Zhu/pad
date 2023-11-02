def solution():
    # Starting number of cans collected
    cans_collected = 20

    # Calculate the total number of cans collected over 5 days
    for i in range(1, 5):
        cans_collected += (5 + i)

    # Calculate the weekly goal for cans collected
    goal_cans_collected = cans_collected * 5
    result = goal_cans_collected
    return result

print(solution())