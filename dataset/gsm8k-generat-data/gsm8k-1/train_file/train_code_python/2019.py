def solution():
    """Bob can shuck 10 oysters in 5 minutes. How many oysters can he shuck in 2 hours?"""
    oysters_per_5min = 10
    minutes_in_2hrs = 120
    oysters_per_2hrs = oysters_per_5min * (minutes_in_2hrs / 5)
    result = oysters_per_2hrs
    return result

print(solution())