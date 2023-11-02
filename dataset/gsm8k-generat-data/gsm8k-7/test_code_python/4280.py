def solution():
    rent_percentage = 0.07  # 7%
    other_expenses_percentage = 0.5 * rent_percentage  # half of rent percentage
    savings_percentage = 1 - rent_percentage - other_expenses_percentage  # remaining percentage for savings
    monthly_earnings =  # your value here

    # Calculate the amount spent on other monthly expenses
    other_expenses = monthly_earnings * other_expenses_percentage

    # Calculate the amount deposited into savings
    savings_amount = monthly_earnings * savings_percentage - 133  # subtract rent amount from savings

    result = savings_amount
    return result

print(solution())