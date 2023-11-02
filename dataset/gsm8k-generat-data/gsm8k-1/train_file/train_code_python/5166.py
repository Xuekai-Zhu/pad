def solution():
    """Malcolm works in a company where they normally pack 40 apples in a box, producing 50 full boxes per day. Operations went as normal in one week. But in the next week, they packed 500 fewer apples per day. What's the total number of apples packed in the two weeks?"""
    normal_apples_per_day = 40 * 50
    normal_week_total = normal_apples_per_day * 7
    reduced_apples_per_day = (40 - (500/50)) * 50
    reduced_week_total = reduced_apples_per_day * 7
    total_apples_packed = normal_week_total + reduced_week_total
    result = total_apples_packed
    return result

print(solution())