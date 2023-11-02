def solution():
    camden_swims = 16
    susannah_swims = 24
    num_weeks = 4

    # Calculate the average number of swims per person per week
    camden_avg = camden_swims / num_weeks
    susannah_avg = susannah_swims / num_weeks

    # Calculate the difference in average number of swims per person per week
    difference = susannah_avg - camden_avg
    result = difference
    return result

print(solution())