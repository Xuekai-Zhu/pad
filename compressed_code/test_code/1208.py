def solution():
    
    current_pay = 30 * 40 * 4
    freelance_pay = 40 * 40 * 4
    fica_taxes = 25 * 4
    healthcare_premiums = 400
    total_freelance_expenses = fica_taxes + healthcare_premiums
    total_freelance_pay = freelance_pay - total_freelance_expenses
    monthly_pay_increase = total_freelance_pay - current_pay
    result = monthly_pay_increase
    return result

print(solution())