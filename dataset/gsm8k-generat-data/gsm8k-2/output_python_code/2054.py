def solution():
    """Sarah makes 5 times more money per hour than Connor does. If Connor earns $7.20 per hour, how much does Sarah make in an 8-hour day?"""
    connor_hourly = 7.20
    sarah_hourly = connor_hourly * 5
    sarah_daily = sarah_hourly * 8
    result = sarah_daily
    return result

print(solution())