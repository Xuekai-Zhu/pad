def solution():
    # Calculate Bill's monthly income
    monthly_income = 25 * 30 * 4  # $25 per hour, 30 hours per week, 4 weeks per month

    # Calculate the government's subsidy based on Bill's income
    if monthly_income < 10000:
        subsidy = 0.9
    elif monthly_income < 40000:
        subsidy = 0.5
    else:
        subsidy = 0.2

    # Calculate the monthly cost of the healthcare plan after the government subsidy
    monthly_cost = 500 * (1 - subsidy)

    # Calculate the annual cost of the healthcare plan after the government subsidy
    annual_cost = monthly_cost * 12
    result = annual_cost
    return result

print(solution())