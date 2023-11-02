def solution():
    # Calculate the total number of apples Archibald eats in the first two weeks
    apples_first_two_weeks = 1 * 14  # 1 apple a day for 2 weeks

    # Calculate the total number of apples Archibald eats in the next three weeks
    apples_next_three_weeks = apples_first_two_weeks * 2  # Same number of apples as first two weeks

    # Calculate the total number of apples Archibald eats in the next two weeks
    apples_next_two_weeks = 3 * 14  # 3 apples a day for 2 weeks

    # Calculate the total number of apples Archibald eats in 7 weeks
    total_apples = apples_first_two_weeks + apples_next_three_weeks + apples_next_two_weeks

    # Calculate the average number of apples Archibald eats per week
    avg_apples_per_week = total_apples / 7
    result = avg_apples_per_week
    return result

print(solution())