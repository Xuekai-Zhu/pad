def solution():
    """John gets his pool cleaned every 3 days. It cost $150 each time and he gives the guy a 10% tip each time he comes to clean. Then twice a month he needs to use $200 of chemicals. How much does his pool cost a month?"""
    cleaning_cost = 150
    tip_percent = 0.1
    chemical_cost = 200
    cleanings_per_month = 30 / 3  # assuming 30-day month
    total_cleaning_cost = cleanings_per_month * cleaning_cost * (1 + tip_percent)
    total_monthly_cost = total_cleaning_cost + chemical_cost
    result = total_monthly_cost
    return result

print(solution())