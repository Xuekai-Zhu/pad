def solution():
    # Calculate the average number of caps made in the first three weeks
    average_caps = (320 + 400 + 300) / 3

    # Calculate the total number of caps made during the fourth week
    fourth_week_caps = average_caps

    # Calculate the total number of caps made in all four weeks
    total_caps = 320 + 400 + 300 + fourth_week_caps
    result = total_caps
    return result

print(solution())