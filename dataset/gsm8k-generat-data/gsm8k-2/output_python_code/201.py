def solution():
    """Archibald eats 1 apple a day for two weeks. Over the next three weeks, he eats the same number of apples as the total of the first two weeks. Over the next two weeks, he eats 3 apples a day. Over these 7 weeks, how many apples does he average a week?"""
    total_apples = 1 * 14 + (1 * 14 * 2) + (3 * 14)
    average_apples_per_week = total_apples / 7
    result = average_apples_per_week
    return result

print(solution())