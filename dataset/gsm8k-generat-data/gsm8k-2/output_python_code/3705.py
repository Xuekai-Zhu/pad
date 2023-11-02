def solution():
    """Bobby received his weekly paycheck today. Although his salary is $450 per week, his actual paycheck is reduced in size because there are some taxes, insurance payments, and fees removed from his pay before his employer writes the check. If the government removes 1/3 in federal taxes and 8% in state taxes, the health insurance removes $50 per week, the life insurance removes $20 per week, and the city charges him a fee of $10 per week for parking, then what is the final amount left in Bobby's paycheck, in dollars?"""
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