def solution():
    """Bobby received his weekly paycheck today. Although his salary is $450 per week, his actual paycheck is reduced in size because there are some taxes, insurance payments, and fees removed from his pay before his employer writes the check. If the government removes 1/3 in federal taxes and 8% in state taxes, the health insurance removes $50 per week, the life insurance removes $20 per week, and the city charges him a fee of $10 per week for parking, then what is the final amount left in Bobby's paycheck, in dollars?"""
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