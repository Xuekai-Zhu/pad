def solution():
    """During the holidays, Lance works as a merchandiser. He works 35 hours a week, spread equally over 5 workdays. If Lance earns $9 an hour, how much does he make on each workday?"""
    hours_per_day = 35 / 5
    hourly_rate = 9
    daily_pay = hours_per_day * hourly_rate
    result = daily_pay
    return result

print(solution())