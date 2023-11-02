def solution():
    """Trisha just got a job offer for an hourly job that pays 15 dollars an hour, 40 hours per week. She has been told to estimate that 20 percent of her pay will be withheld to pay taxes, unemployment insurance, and social security. Assuming Trisha works 52 weeks in a year, what is her annual "take-home" pay?"""
    hourly_pay = 15
    weekly_hours = 40
    weeks_per_year = 52
    withholding_percent = 0.2
    annual_income = hourly_pay * weekly_hours * weeks_per_year
    withholding_amount = annual_income * withholding_percent
    take_home_pay = annual_income - withholding_amount
    result = take_home_pay
    return result

print(solution())