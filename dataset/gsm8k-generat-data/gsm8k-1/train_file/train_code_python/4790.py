def solution():
    """A cougar is sleeping for 4 hours at night, and a zebra for 2 hours more. How much time do both animals sleep in one week?"""
    cougar_sleep = 4
    zebra_sleep = cougar_sleep + 2
    days_per_week = 7
    total_sleep = (cougar_sleep + zebra_sleep) * days_per_week
    result = total_sleep
    return result

print(solution())