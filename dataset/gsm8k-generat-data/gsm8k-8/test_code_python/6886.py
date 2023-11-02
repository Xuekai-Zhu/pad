def solution():
    # Calculate the total number of caps made in the first three weeks
    total_caps = 320 + 400 + 300

    # Calculate the average number of caps made per week in the first three weeks
    average_caps_per_week = total_caps / 3

    # Calculate the total number of caps made in the fourth week
    total_caps_fourth_week = 4 * average_caps_per_week

    result = total_caps_fourth_week
    return result

print(solution())