def solution():
    # Calculate Alex's tax deduction
    tax_deduction = 0.1 * 500

    # Calculate Alex's tithe
    tithe = 0.1 * 500

    # Calculate Alex's total expenses
    total_expenses = tax_deduction + 55 + tithe

    # Calculate Alex's remaining money
    remaining_money = 500 - total_expenses

    result = remaining_money
    return result

print(solution())