def solution():
    # Calculate Bill's monthly income
    hourly_rate = 25
    weekly_hours = 30
    monthly_income = hourly_rate * weekly_hours * 4

    # Determine government subsidy based on income
    if monthly_income < 10000:
        subsidy = 0.9
    elif monthly_income >= 10001 and monthly_income <= 40000:
        subsidy = 0.5
    elif monthly_income > 50000:
        subsidy = 0.2
    else:
        subsidy = 0

    # Calculate Bill's monthly cost for insurance
    full_price = 500
    subsidized_price = full_price * (1 - subsidy)
    monthly_cost = subsidized_price

    # Calculate Bill's yearly cost for insurance
    yearly_cost = monthly_cost * 12

    result = yearly_cost
    return result

print(solution())