def solution():
    """Mitch is a freelancer, she works 5 hours every day from Monday to Friday and 3 hours every Saturday and Sunday. If she earns $3 per hour and earns double on weekends, how much does she earn every week?"""
    weekday_hours = 5 * 5 # 5 hours per day, 5 days a week
    weekend_hours = 3 * 2 + 3 * 2 # 3 hours each on Saturday and Sunday, earning double
    weekday_pay = weekday_hours * 3 # $3 per hour
    weekend_pay = weekend_hours * 6 # $6 per hour on weekends
    weekly_pay = weekday_pay + weekend_pay
    result = weekly_pay
    return result

print(solution())