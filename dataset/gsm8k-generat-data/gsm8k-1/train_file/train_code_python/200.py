def solution():
    """Archibald eats 1 apple a day for two weeks. Over the next three weeks, he eats the same number of apples as the total of the first two weeks. Over the next two weeks, he eats 3 apples a day. Over these 7 weeks, how many apples does he average a week?"""
    first_two_weeks = 14
    next_three_weeks = first_two_weeks * 2
    next_two_weeks = 14
    total_weeks = 7
    total_apples = first_two_weeks + next_three_weeks + next_two_weeks * 3
    average_apples_per_week = total_apples / total_weeks
    result = average_apples_per_week
    return result

print(solution())