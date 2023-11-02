def solution():
    annual_income = 60000
    tax_rate = 0.18  # 18% tax rate

    # Calculate the amount of taxes to be paid
    tax_amount = annual_income * tax_rate

    # Calculate the amount of money Dorothy will have left after paying taxes
    net_income = annual_income - tax_amount
    result = net_income
    return result

print(solution())