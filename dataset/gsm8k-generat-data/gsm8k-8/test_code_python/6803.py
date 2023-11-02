def solution():
    # Calculate the profit made each month
    monthly_profit = 4000 - 1500

    # Calculate the number of months needed to make back the initial cost
    months_to_pay_back = 25000 / monthly_profit

    result = months_to_pay_back
    return result

print(solution())