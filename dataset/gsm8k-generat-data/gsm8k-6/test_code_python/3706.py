def solution():
    # Calculate the total deductions from Bobby's salary
    federal_tax = (1/3) * 450
    state_tax = 0.08 * 450
    health_insurance = 50
    life_insurance = 20
    city_fee = 10
    total_deductions = federal_tax + state_tax + health_insurance + life_insurance + city_fee

    # Calculate the final amount in Bobby's paycheck
    final_amount = 450 - total_deductions
    result = final_amount
    return result

print(solution())