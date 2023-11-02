def solution():
    """Jamie earns $10 an hour by delivering flyers. She delivers flyers 2 days each week. It takes her 3 hours each time she delivers flyers. After delivering flyers for 6 weeks, how much money will she have earned?"""
    # Define Jamie's pay rate and delivery schedule
    PAY_RATE = 10
    DELIVERY_DAYS_PER_WEEK = 2
    HOURS_PER_DELIVERY = 3

    # Calculate the total number of deliveries Jamie will make over 6 weeks
    num_deliveries = DELIVERY_DAYS_PER_WEEK * 6

    # Calculate the total number of hours Jamie will work
    total_hours = num_deliveries * HOURS_PER_DELIVERY

    # Calculate Jamie's total earnings
    earnings = total_hours * PAY_RATE

    # Display Jamie's total earnings
    result = earnings
    return result

print(solution())