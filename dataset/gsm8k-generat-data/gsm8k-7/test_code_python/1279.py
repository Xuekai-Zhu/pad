def solution():
    monthly_cost = 500
    hourly_pay = 25
    hours_per_week = 30
    weeks_per_month = 4

    # Calculate Bill's annual income
    annual_income = hourly_pay * hours_per_week * weeks_per_month * 12

    # Determine the percentage of the cost that the government will pay based on Bill's income
    if annual_income < 10000:
        government_percent = 0.9
    elif 10001 <= annual_income <= 40000:
        government_percent = 0.5
    else:
        government_percent = 0.2

    # Calculate Bill's out-of-pocket monthly cost based on the government's contribution
    monthly_out_of_pocket = monthly_cost * (1 - government_percent)

    # Calculate Bill's annual out-of-pocket cost
    annual_out_of_pocket = monthly_out_of_pocket * 12
    result = annual_out_of_pocket
    return result

print(solution())