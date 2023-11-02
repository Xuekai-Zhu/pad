def solution():
    first_week_caps = 320
    second_week_caps = 400
    third_week_caps = 300

    # Calculate the total number of caps made in the first three weeks
    total_caps_first_three_weeks = first_week_caps + second_week_caps + third_week_caps

    # Calculate the average number of caps made in the first three weeks
    average_caps_first_three_weeks = total_caps_first_three_weeks / 3

    # Calculate the total number of caps made in the fourth week to match the average of the first three weeks
    fourth_week_caps = average_caps_first_three_weeks * 4 - total_caps_first_three_weeks

    # Calculate the total number of caps made in all four weeks
    total_caps = total_caps_first_three_weeks + fourth_week_caps
    result = total_caps
    return result

print(solution())