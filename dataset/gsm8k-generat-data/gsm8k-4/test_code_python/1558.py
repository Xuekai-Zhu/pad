def solution():
    """Janet is trying to decide whether to quit her job and start freelancing. She works 40 hours a week at both jobs. She get paid $30/hour at her current job, and would get paid $40/hour as a freelancer. However, she'd have to pay an extra $25 a week in FICA taxes plus $400/month in healthcare premiums. How much more would Janet make per month as a freelancer if there are four weeks in a month?"""
    # Define the hourly wage at Janet's current job and as a freelancer
    current_wage = 30
    freelancer_wage = 40

    # Define the number of hours worked per week
    hours_per_week = 40

    # Calculate the weekly income at Janet's current job and as a freelancer
    current_income_weekly = current_wage * hours_per_week
    freelancer_income_weekly = freelancer_wage * hours_per_week - 25

    # Calculate the monthly income at Janet's current job and as a freelancer
    current_income_monthly = current_income_weekly * 4
    freelancer_income_monthly = freelancer_income_weekly * 4 - 400

    # Calculate the difference in income between the two jobs
    income_difference = freelancer_income_monthly - current_income_monthly

    # Return the result
    result = income_difference
    return result

print(solution())