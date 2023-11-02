def solution():
    """James rents his car out for $20 an hour.  He rents it for 8 hours a day 4 days a week.  How much does he make a week?"""
    # Define the rental rate per hour
    RENTAL_RATE = 20

    # Define the number of hours James rents out his car each day
    rental_hours_per_day = 8

    # Define the number of days James rents out his car each week
    rental_days_per_week = 4

    # Calculate the total number of rental hours per week
    rental_hours_per_week = rental_hours_per_day * rental_days_per_week

    # Calculate James' weekly earnings
    weekly_earnings = rental_hours_per_week * RENTAL_RATE

    # Display James' weekly earnings
    result = weekly_earnings
    return result

print(solution())