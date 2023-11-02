def solution():
    """Sarah makes 5 times more money per hour than Connor does. If Connor earns $7.20 per hour, how much does Sarah make in an 8-hour day?"""
    connor_hourly_wage = 7.20
    sarah_hourly_wage = connor_hourly_wage * 5
    sarah_daily_earnings = sarah_hourly_wage * 8
    result = sarah_daily_earnings
    return result

print(solution())