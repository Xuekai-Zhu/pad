def solution():
    """During the holidays, Lance works as a merchandiser. He works 35 hours a week, spread equally over 5 workdays. If Lance earns $9 an hour, how much does he make on each workday?"""
    weekly_hours = 35
    workdays = 5
    daily_hours = weekly_hours / workdays
    hourly_wage = 9
    daily_wage = daily_hours * hourly_wage
    result = daily_wage
    return result

print(solution())