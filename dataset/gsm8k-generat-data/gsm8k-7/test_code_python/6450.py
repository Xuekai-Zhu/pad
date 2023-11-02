def solution():
    hourly_pay = 15
    num_hours_per_week = 40
    num_weeks_per_year = 52
    tax_withhold_rate = 0.2

    # Calculate Trisha's gross annual pay
    gross_pay = hourly_pay * num_hours_per_week * num_weeks_per_year

    # Calculate the amount withheld for taxes, unemployment insurance, and social security
    withhold_amount = gross_pay * tax_withhold_rate

    # Calculate Trisha's annual take-home pay
    take_home_pay = gross_pay - withhold_amount
    result = take_home_pay
    return result

print(solution())