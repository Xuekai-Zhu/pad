def solution():
    
    annual_salary = 150000
    savings_rate = 0.1
    downpayment_percent = 0.2
    house_cost = 450000
    downpayment_amount = house_cost * downpayment_percent
    yearly_savings = annual_salary * savings_rate
    years_to_save = downpayment_amount / yearly_savings
    result = years_to_save
    
    return result

print(solution())