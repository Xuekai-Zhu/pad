def solution():
    """Susan is taking a two week vacation. She works five days a week and has six days of paid vacation. The rest of her workdays will be unpaid vacation time. She gets paid $15 per hour and works 8 hours a day. How much pay will she miss on her vacation?"""
    # Define the number of days Susan works in a week and the number of paid vacation days
    WORKDAYS_PER_WEEK = 5
    PAID_VACATION_DAYS = 6

    # Define the pay rate and number of hours worked per day
    PAY_RATE = 15
    HOURS_PER_DAY = 8

    # Calculate the total number of workdays Susan has in two weeks
    total_workdays = WORKDAYS_PER_WEEK * 2 - PAID_VACATION_DAYS

    # Calculate the total pay Susan will miss on her vacation
    missed_pay = total_workdays * HOURS_PER_DAY * PAY_RATE

    # Display the missed pay
    result = missed_pay
    return result

print(solution())