def solution():
    """Jamie earns $10 an hour by delivering flyers. She delivers flyers 2 days each week. It takes her 3 hours each time she delivers flyers. After delivering flyers for 6 weeks, how much money will she have earned?"""
    # Define Jamie's hourly rate and the number of hours she works each week
    hourly_rate = 10
    hours_per_week = 6

    # Define the number of days Jamie delivers flyers each week and the time it takes her to deliver flyers each day
    delivery_days_per_week = 2
    delivery_hours_per_day = 3

    # Calculate Jamie's total earnings for one week of flyer delivery
    earnings_per_week = hourly_rate * hours_per_week * delivery_days_per_week * delivery_hours_per_day

    # Calculate Jamie's total earnings for 6 weeks of flyer delivery
    total_earnings = earnings_per_week * 6

    # return the result
    result = total_earnings
    return result

print(solution())