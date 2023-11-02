def solution():
    
    salary = 450
    fed_tax = 1/3
    state_tax = 0.08
    health_insurance = 50
    life_insurance = 20
    city_parking_fee = 10
    total_tax = salary * (fed_tax + state_tax)
    total_deductions = total_tax + health_insurance + life_insurance + city_parking_fee
    final_paycheck = salary - total_deductions
    result = final_paycheck
    return result

print(solution())