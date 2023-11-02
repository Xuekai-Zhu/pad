def solution():
    """Last week, Arman worked 35 hours for 5 days at $10 per hour. This week, he will receive an increase of $0.5 per hour if he can work for 40 hours. Suppose he can work for 40 hours this week, how much will Arman receive for working two weeks?"""
    last_week_hours = 35
    last_week_pay = last_week_hours * 10
    this_week_hours = 40
    this_week_pay = (this_week_hours * 10.5)
    total_pay = last_week_pay + this_week_pay
    result = total_pay
    return result

print(solution())