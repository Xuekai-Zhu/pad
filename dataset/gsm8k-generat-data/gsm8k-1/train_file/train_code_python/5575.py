def solution():
    """Mitch is a freelancer, she works 5 hours every day from Monday to Friday and 3 hours every Saturday and Sunday. If she earns $3 per hour and earns double on weekends, how much does she earn every week?"""
    weekday_hours = 5
    weekend_hours = 3
    weekday_pay = 3
    weekend_pay = weekday_pay * 2
    weekly_pay = (weekday_hours * weekday_pay * 5) + (weekend_hours * weekend_pay * 2)
    result = weekly_pay
    return result

print(solution())