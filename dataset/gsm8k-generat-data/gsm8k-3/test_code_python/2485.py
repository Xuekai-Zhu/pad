def solution():
    """Carly practices her butterfly stroke for 3 hours a day, 4 days a week, and her backstroke for 2 hours a day, six days a week. How much time does she spend practicing swimming in a month with 4 weeks?"""
    # Calculate the total number of hours Carly practices butterfly stroke in a week
    butterfly_weekly_hours = 3 * 4

    # Calculate the total number of hours Carly practices backstroke in a week
    backstroke_weekly_hours = 2 * 6

    # Calculate the total number of hours Carly practices swimming in a week
    weekly_hours = butterfly_weekly_hours + backstroke_weekly_hours

    # Calculate the total number of hours Carly practices swimming in a month
    monthly_hours = weekly_hours * 4

    # Display the total number of hours Carly practices swimming in a month
    result = monthly_hours
    return result

print(solution())