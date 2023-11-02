def solution():
    
    monthly_healthcare_cost = 500
    annual_income = 25 * 30 * 4 * 12 
    if annual_income < 10000:
        government_contribution = monthly_healthcare_cost * 0.9
    elif annual_income < 40000:
        government_contribution = monthly_healthcare_cost * 0.5
    elif annual_income > 50000:
        government_contribution = monthly_healthcare_cost * 0.2
    else:
        government_contribution = 0
    bill_amount = monthly_healthcare_cost - government_contribution
    total_cost = bill_amount * 12
    result = total_cost
    return result

print(solution())