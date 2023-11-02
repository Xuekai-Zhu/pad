def solution():
    """Tim's website got 100 visitors a day for the first 6 days and then on the last day of the week it got twice as many visitors as every other day combined.  If he gets $.01 per visit how much did he make that week?"""
    # Define the number of visitors per day and the pay per visit
    DAILY_VISITORS = 100
    PAY_PER_VISIT = 0.01

    # Calculate the total number of visitors for the first 6 days
    visitors_first_six_days = DAILY_VISITORS * 6

    # Calculate the total number of visitors for the last day
    visitors_last_day = (visitors_first_six_days * 2) - visitors_first_six_days

    # Calculate the total number of visitors for the week
    total_visitors = visitors_first_six_days + visitors_last_day

    # Calculate the total earnings for the week
    total_earnings = total_visitors * PAY_PER_VISIT

    # Display the total earnings
    result = total_earnings
    return result

print(solution())