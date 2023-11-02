def solution():
    week1_caps = 320
    week2_caps = 400
    week3_caps = 300

    # Calculate the total number of caps made in the first three weeks
    total_caps = week1_caps + week2_caps + week3_caps

    # Calculate the average number of caps made per week in the first three weeks
    avg_caps_per_week = total_caps / 3

    # Calculate the total number of caps made in the fourth week assuming the same average
    caps_week4 = avg_caps_per_week

    # Calculate the total number of caps made in all four weeks
    total_caps_all_weeks = total_caps + caps_week4
    result = total_caps_all_weeks
    return result

print(solution())