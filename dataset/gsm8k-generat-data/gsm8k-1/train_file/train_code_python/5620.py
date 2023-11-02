def solution():
    """Lawrence worked 8 hours each day on Monday, Tuesday and Friday. He worked 5.5 hours on both Wednesday and Thursday. How many hours would Lawrence work each day if he worked the same number of hours each day?"""
    weekly_hours = 8 * 3 + 5.5 * 2
    daily_hours = weekly_hours / 5
    result = daily_hours
    return result

print(solution())