def solution():
    """Chandler can eat a total of 23 apples and Lucy can eat a total of 19 apples per week. If the farmer only delivers 1 time per month, how many apples do they have to order for a month?"""
    chandler_weekly_apples = 23
    lucy_weekly_apples = 19
    total_weekly_apples = chandler_weekly_apples + lucy_weekly_apples
    apples_per_month = total_weekly_apples * 4
    result = apples_per_month
    return result

print(solution())