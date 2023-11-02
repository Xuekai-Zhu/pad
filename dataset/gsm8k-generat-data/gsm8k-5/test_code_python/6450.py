def solution():
    hourly_pay = 15  # Trisha earns 15 dollars per hour
    hours_per_week = 40  # Trisha works 40 hours per week
    weeks_per_year = 52  # Trisha works 52 weeks per year
    withholding_percent = 0.2  # 20% of Trisha's pay will be withheld

    # Calculate Trisha's gross pay per week
    gross_pay_per_week = hourly_pay * hours_per_week

    # Calculate Trisha's total gross pay for the year
    total_gross_pay = gross_pay_per_week * weeks_per_year

    # Calculate the amount withheld from Trisha's pay
    withholding_amount = total_gross_pay * withholding_percent

    # Calculate Trisha's annual take-home pay
    annual_take_home_pay = total_gross_pay - withholding_amount
    result = annual_take_home_pay
    return result

print(solution())