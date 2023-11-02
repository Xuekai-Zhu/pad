def solution():
    hourly_rate = 5  # Julie's hourly rate is $5
    hours_per_day = 8  # Julie works 8 hours per day
    days_per_week = 6  # Julie works 6 days per week
    days_in_month = 30  # Assume there are 30 days in a month
    days_missed = 1  # Julie missed a day of work

    # Calculate the total number of hours Julie worked in a month
    total_hours = (hours_per_day * days_per_week * days_in_month) - (hours_per_day * days_missed)

    # Calculate Julie's monthly salary
    monthly_salary = total_hours * hourly_rate
    result = monthly_salary
    return result

print(solution())