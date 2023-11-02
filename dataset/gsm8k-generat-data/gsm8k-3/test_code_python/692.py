def solution():
    """Edric's monthly salary is $576. If he works 8 hours a day for 6 days a week, how much is his hourly rate?"""
    # Calculate the total number of hours worked in a month
    hours_per_day = 8
    days_per_week = 6
    weeks_per_month = 4
    total_hours = hours_per_day * days_per_week * weeks_per_month

    # Calculate Edric's hourly rate
    salary_per_month = 576
    hourly_rate = salary_per_month / total_hours

    # Display Edric's hourly rate
    result = hourly_rate
    return result

print(solution())