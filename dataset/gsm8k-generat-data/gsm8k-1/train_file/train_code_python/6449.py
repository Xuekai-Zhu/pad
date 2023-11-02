def solution():
    """Trisha just got a job offer for an hourly job that pays 15 dollars an hour, 40 hours per week. She has been told to estimate that 20 percent of her pay will be withheld to pay taxes, unemployment insurance, and social security. Assuming Trisha works 52 weeks in a year, what is her annual "take-home" pay?"""
    hourly_wage = 15
    hours_per_week = 40
    weeks_per_year = 52
    percentage_withheld = 0.20
    gross_yearly_income = hourly_wage * hours_per_week * weeks_per_year
    withheld_amount = gross_yearly_income * percentage_withheld
    take_home_pay = gross_yearly_income - withheld_amount
    result = take_home_pay
    return result

print(solution())