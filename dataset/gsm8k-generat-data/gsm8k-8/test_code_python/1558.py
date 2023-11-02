def solution():
    # Define the hourly rates and weekly hours
    current_rate = 30
    freelance_rate = 40
    weekly_hours = 40

    # Calculate the weekly pay for both jobs
    current_weekly_pay = current_rate * weekly_hours
    freelance_weekly_pay = freelance_rate * weekly_hours

    # Calculate the extra expenses for freelancing
    extra_expenses = 25 + 400/4

    # Calculate the monthly take-home pay for both jobs
    current_monthly_pay = current_weekly_pay * 4
    freelance_monthly_pay = (freelance_weekly_pay - extra_expenses) * 4

    # Calculate the difference in monthly pay
    monthly_difference = freelance_monthly_pay - current_monthly_pay
    result = monthly_difference
    return result

print(solution())