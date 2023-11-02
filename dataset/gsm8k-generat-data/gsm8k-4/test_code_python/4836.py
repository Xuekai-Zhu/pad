def solution():
    """Jon runs a website where he gets paid for every person who visits. He gets paid $0.10 for every person who visits.
    Each hour he gets 50 visits. His website operates 24 hours a day. How many dollars does he make in a 30 day month?"""
    # Define the number of hours in a day and the number of days in a month
    HOURS_PER_DAY = 24
    DAYS_PER_MONTH = 30

    # Define the payment per visits and the number of visits per hour
    PAYMENT_PER_VISIT = 0.10
    VISITS_PER_HOUR = 50

    # Calculate the number of visits per day and per month
    visits_per_day = VISITS_PER_HOUR * HOURS_PER_DAY
    visits_per_month = visits_per_day * DAYS_PER_MONTH

    # Calculate the total earnings in a month
    earnings_per_month = visits_per_month * PAYMENT_PER_VISIT

    # return the result
    result = earnings_per_month
    return result

print(solution())