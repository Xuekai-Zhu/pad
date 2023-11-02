def solution():
    """Malcolm works in a company where they normally pack 40 apples in a box, producing 50 full boxes per day. Operations went as normal in one week. But in the next week, they packed 500 fewer apples per day. What's the total number of apples packed in the two weeks?"""
    normal_daily_production = 40 * 50
    normal_weekly_production = normal_daily_production * 7
    reduced_daily_production = normal_daily_production - 500
    reduced_weekly_production = reduced_daily_production * 7
    total_production = normal_weekly_production + reduced_weekly_production
    result = total_production
    return result

print(solution())