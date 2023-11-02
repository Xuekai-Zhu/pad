def solution():
    """Susan is taking a two week vacation. She works five days a week and has six days of paid vacation. The rest of her workdays will be unpaid vacation time. She gets paid $15 per hour and works 8 hours a day. How much pay will she miss on her vacation?"""
    # Define Susan's workweek and vacation time
    WORK_WEEK = 5
    PAID_VACATION = 6
    TOTAL_VACATION = 10

    # Define Susan's hourly rate and working hours per day
    HOURLY_RATE = 15
    WORK_HOURS = 8

    # Calculate Susan's total working hours during her two-week vacation
    total_working_hours = (WORK_WEEK * 2) - PAID_VACATION

    # Calculate the pay Susan will miss out on during her vacation
    missed_pay = total_working_hours * WORK_HOURS * HOURLY_RATE

    # return the result
    result = missed_pay
    return result

print(solution())