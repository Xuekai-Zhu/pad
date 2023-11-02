def solution():
    # Calculate the total number of apples eaten in the first two weeks
    apples_first_two_weeks = 14

    # Calculate the total number of apples eaten in the next three weeks
    apples_next_three_weeks = apples_first_two_weeks

    # Calculate the total number of apples eaten in the next two weeks
    apples_next_two_weeks = 3 * 14

    # Calculate the total number of apples eaten over 7 weeks
    total_apples = apples_first_two_weeks + apples_next_three_weeks + apples_next_two_weeks

    # Calculate the average number of apples eaten per week
    average_apples_per_week = total_apples / 7
    result = average_apples_per_week
    return result

print(solution())