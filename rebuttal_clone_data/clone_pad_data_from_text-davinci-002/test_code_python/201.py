def solution():
    """Archibald eats 1 apple a day for two weeks. Over the next three weeks, he eats the same number of apples as the total of the first two weeks. Over the next two weeks, he eats 3 apples a day. Over these 7 weeks, how many apples does he average a week?"""
    apples_first_two_weeks = 2 * 7
    apples_next_three_weeks = apples_first_two_weeks * 3
    apples_next_two_weeks = 2 * 3 * 7
    total_weeks = 2 + 3 + 2
    total_apples = apples_first_two_weeks + apples_next_three_weeks + apples_next_two_weeks
    average_apples = total_apples / total_weeks
    result = average_apples
    return result

print(solution())