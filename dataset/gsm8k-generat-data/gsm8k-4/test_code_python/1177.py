def solution():
    """James rents his car out for $20 an hour. He rents it for 8 hours a day 4 days a week. How much does he make a week?"""
    # Define the rental rate and the number of hours rented per week
    rental_rate = 20
    rental_hours_weekly = 8 * 4

    # Calculate the total weekly earnings
    weekly_earnings = rental_rate * rental_hours_weekly

    result = weekly_earnings
    return result

print(solution())