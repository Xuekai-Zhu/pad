def solution():
    
    salary = 450
    federal_tax = salary * (1/3)
    state_tax = salary * (8/100)
    health_insurance = 50
    life_insurance = 20
    parking_fee = 10
    
    total_deductions = federal_tax + state_tax + health_insurance + life_insurance + parking_fee
    final_paycheck = salary - total_deductions
    
    result = final_paycheck
    return result

print(solution())