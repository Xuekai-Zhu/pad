def solution():
    """Trisha just got a job offer for an hourly job that pays 15 dollars an hour, 40 hours per week. She has been told to estimate that 20 percent of her pay will be withheld to pay taxes, unemployment insurance, and social security. Assuming Trisha works 52 weeks in a year, what is her annual "take-home" pay?"""
    # Define the hourly wage and the number of hours worked per week
    hourly_wage = 15
    weekly_hours = 40

    # Calculate the weekly pay before taxes
    weekly_pay = hourly_wage * weekly_hours

    # Calculate the weekly pay after taxes
    weekly_takehome_pay = weekly_pay * (1-0.2)

    # Calculate the annual take-home pay
    annual_takehome_pay = weekly_takehome_pay * 52

    # return the result
    result = annual_takehome_pay
    return result

print(solution())