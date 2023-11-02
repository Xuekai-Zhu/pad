def solution():
    basic_salary = 1250
    commission_rate = 0.1
    total_sales = 23600
    savings_percentage = 0.2

    # Calculate Robert's total earnings
    total_earnings = basic_salary + (commission_rate * total_sales)

    # Calculate the amount of money Robert saved
    savings_amount = savings_percentage * total_earnings

    # Calculate the amount of money Robert spent on monthly expenses
    expenses = total_earnings - savings_amount
    result = expenses
    return result

print(solution())