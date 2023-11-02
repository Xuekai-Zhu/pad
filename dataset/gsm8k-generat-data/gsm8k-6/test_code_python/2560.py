def solution():
    balance = 150
    finance_charge = 0.02 * balance  # 2% finance charge
    total_balance = balance + finance_charge
    result = total_balance
    return result

print(solution())