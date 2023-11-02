def solution():
    """A cougar is sleeping for 4 hours at night, and a zebra for 2 hours more. How much time do both animals sleep in one week?"""
    cougar_sleep = 4
    zebra_sleep = 6
    total_sleep_per_night = cougar_sleep + zebra_sleep
    total_sleep_per_week = total_sleep_per_night * 7
    result = total_sleep_per_week
    return result

print(solution())