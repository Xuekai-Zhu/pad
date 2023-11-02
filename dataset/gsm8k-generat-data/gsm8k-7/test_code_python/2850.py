def solution():
    monthly_income = 2000
    transport_percentage = 0.05

    # Calculate the monthly transport expense
    transport_expense = monthly_income * transport_percentage

    # Calculate the remaining amount after deducting the transport expense from the income
    remaining_amount = monthly_income - transport_expense
    result = remaining_amount
    return result

print(solution())