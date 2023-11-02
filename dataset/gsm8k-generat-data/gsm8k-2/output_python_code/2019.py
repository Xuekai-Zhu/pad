def solution():
    """Bob can shuck 10 oysters in 5 minutes. How many oysters can he shuck in 2 hours?"""
    oysters_per_minute = 10/5 # 2 oysters per minute
    total_minutes = 2 * 60 # 2 hours in minutes
    total_oysters = oysters_per_minute * total_minutes
    result = total_oysters
    return result

print(solution())