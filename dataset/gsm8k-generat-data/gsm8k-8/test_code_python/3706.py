def solution():
    # Define the starting salary
    starting_salary = 450

    # Calculate the federal tax deduction
    federal_tax = starting_salary * (1/3)

    # Calculate the state tax deduction
    state_tax = starting_salary * 0.08

    # Calculate the total deductions
    total_deductions = federal_tax + state_tax + 50 + 20 + 10

    # Calculate the final paycheck amount
    final_paycheck = starting_salary - total_deductions
    result = final_paycheck
    return result

print(solution())