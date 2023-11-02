def solution():
    rate_per_hour = 60  # The magician charges $60 per hour
    hours_per_day = 3  # The magician works 3 hours per day
    days_per_week = 7  # There are 7 days in a week
    weeks = 2  # The magician works for 2 weeks

    # Calculate the total number of hours the magician works
    total_hours = hours_per_day * days_per_week * weeks

    # Calculate the total amount Stan pays the magician
    total_payment = total_hours * rate_per_hour
    result = total_payment
    return result

print(solution())