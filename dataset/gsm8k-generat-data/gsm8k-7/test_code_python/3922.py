def solution():
    current_production = 100 # cars per month
    target_production = 1800 # cars per year

    # Calculate the current annual production rate
    current_annual_production = current_production * 12

    # Calculate the additional monthly production needed to reach the target
    additional_production = (target_production - current_annual_production) / 12

    result = round(additional_production)
    return result

print(solution())