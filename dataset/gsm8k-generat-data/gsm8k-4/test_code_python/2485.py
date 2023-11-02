def solution():
    """Carly practices her butterfly stroke for 3 hours a day, 4 days a week, and her backstroke for 2 hours a day, six days a week. How much time does she spend practicing swimming in a month with 4 weeks?"""
    # Define the number of hours per day Carly practices
    butterfly_hours = 3
    backstroke_hours = 2

    # Define the number of days per week Carly practices
    butterfly_days = 4
    backstroke_days = 6

    # Calculate the total hours Carly practices per week
    weekly_hours = (butterfly_hours * butterfly_days) + (backstroke_hours * backstroke_days)

    # Calculate the total hours Carly practices per month
    monthly_hours = weekly_hours * 4

    # Return the result
    result = monthly_hours
    return result

print(solution())