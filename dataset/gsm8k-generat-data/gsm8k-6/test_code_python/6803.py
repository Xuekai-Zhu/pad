def solution():
    # Calculate the profit made by Kim each month
    profit_per_month = 4000 - 1500  # revenue minus expenses

    # Calculate the number of months it will take to pay back the cost
    months_to_pay_back = 25000 / profit_per_month

    result = months_to_pay_back
    return result

print(solution())