def solution():
    # Define Maria's monthly salary
    salary = 2000

    # Calculate the amount of money taken for tax and insurance
    tax = 0.2 * salary
    insurance = 0.05 * salary

    # Calculate the amount of money left after tax and insurance deductions
    remaining_money = salary - tax - insurance

    # Calculate the amount spent on utility bills
    utility_bills = 0.25 * remaining_money

    # Calculate the final amount of money Maria has after deductions and utility bills payment
    final_amount = remaining_money - utility_bills

    result = final_amount
    return result

print(solution())