def solution():
    """John gets his pool cleaned every 3 days. It cost $150 each time and he gives the guy a 10% tip each time he comes to clean. Then twice a month he needs to use $200 of chemicals. How much does his pool cost a month?"""
    cleaning_cost = 150
    tip_percent = 10
    tip_amount = cleaning_cost * (tip_percent / 100)
    total_cleaning_cost = cleaning_cost + tip_amount
    cleanings_per_month = 30 / 3 # assuming 30-day month
    monthly_cleaning_cost = total_cleaning_cost * cleanings_per_month
    chemical_cost = 200
    total_cost = monthly_cleaning_cost + chemical_cost
    result = total_cost
    return result

print(solution())