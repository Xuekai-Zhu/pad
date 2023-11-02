def solution():
    """Janet is trying to decide whether to quit her job and start freelancing. She works 40 hours a week at both jobs. She make $30/hour at her current job, and would make $40/hour as a freelancer. However, she'd have to pay an extra $25 a week in FICA taxes plus $400/month in healthcare premiums. How much more would Janet make per month as a freelancer if there are four weeks in a month?"""
    # Define the number of hours Janet works per week
    hours_per_week = 40

    # Define the pay rates
    current_job_pay = 30
    freelance_pay = 40

    # Define the additional costs for freelancing
    fica_taxes = 25 * 4
    healthcare_premiums = 400

    # Calculate the monthly earnings at Janet's current job
    current_monthly_earnings = hours_per_week * current_job_pay * 4

    # Calculate the monthly earnings as a freelancer
    freelancer_monthly_earnings = (hours_per_week * freelance_pay * 4) - fica_taxes - healthcare_premiums

    # Determine how much more Janet would make as a freelancer
    difference = freelancer_monthly_earnings - current_monthly_earnings

    # Display the difference in earnings
    result = difference
    return result

print(solution())