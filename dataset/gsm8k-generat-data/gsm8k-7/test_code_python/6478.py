def solution():
    week_1_growth = 2
    week_2_growth = week_1_growth * 2
    week_3_growth = week_2_growth * 4

    total_growth = week_1_growth + week_2_growth + week_3_growth
    height = total_growth + 2  # add the initial height of the plants

    result = height
    return result

print(solution())