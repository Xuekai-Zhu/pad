def solution():
    
    annual_salary = 150000
    savings_percentage = 0.1
    savings_per_year = annual_salary * savings_percentage
    house_cost = 450000
    downpayment_percentage = 0.2
    downpayment_amount = house_cost * downpayment_percentage
    years_to_save = downpayment_amount / savings_per_year
    result = years_to_save
    return result

print(solution())