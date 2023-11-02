def solution():
    # Find the number of oysters shucked in 2 hours
    time_in_minutes = 2 * 60  # 2 hours in minutes
    rate_in_minutes = 5  # Bob can shuck 10 oysters in 5 minutes
    oysters_shucked = (time_in_minutes / rate_in_minutes) * 10
    result = oysters_shucked
    return result

print(solution())