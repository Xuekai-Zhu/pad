def solution():
    normal_monthly_price = 500
    government_subsidy_percentage = [90, 50, 20]
    bill_hourly_rate = 25
    bill_hours_worked_per_week = 30
    bill_weeks_worked_per_month = 4
    bill_monthly_income = bill_hourly_rate * bill_hours_worked_per_week * \
    bill_weeks_worked_per_month
    
    # Determine government subsidy amount
    if bill_monthly_income <= 10000:
        government_subsidy = normal_monthly_price * \
        (government_subsidy_percentage[0]/100)
    elif bill_monthly_income <= 40000:
        government_subsidy = normal_monthly_price * \
        (government_subsidy_percentage[1]/100)
    else:
        government_subsidy = normal_monthly_price * \
        (government_subsidy_percentage[2]/100)
        
    # Subtract government

print(solution())