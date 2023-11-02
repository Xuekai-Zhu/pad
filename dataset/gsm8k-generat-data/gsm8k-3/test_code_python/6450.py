def solution():
    """Trisha just got a job offer for an hourly job that pays 15 dollars an hour, 40 hours per week. She has been told to estimate that 20 percent of her pay will be withheld to pay taxes, unemployment insurance, and social security. Assuming Trisha works 52 weeks in a year, what is her annual "take-home" pay?"""
    # Define Trisha's hourly rate and weekly work hours
    HOURLY_RATE = 15
    WEEKLY_HOURS = 40

    # Calculate Trisha's gross annual income
    gross_income = HOURLY_RATE * WEEKLY_HOURS * 52

    # Calculate the amount withheld for taxes, unemployment insurance, and social security
    withholdings = gross_income * 0.2

    # Calculate Trisha's annual take-home pay
    take_home_pay = gross_income - withholdings

    # Display Trisha's annual take-home pay
    result = take_home_pay
    return result

print(solution())