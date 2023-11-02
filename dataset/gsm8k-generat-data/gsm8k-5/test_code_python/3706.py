def solution():
    # Calculate the federal tax deduction
    federal_tax = 450 * (1/3)

    # Calculate the state tax deduction
    state_tax = 0.08 * 450

    # Calculate the total deductions
    total_deductions = federal_tax + state_tax + 50 + 20 + 10

    # Calculate the final amount in Bobby's paycheck
    final_amount = 450 - total_deductions
    result = final_amount
    return result

print(solution())