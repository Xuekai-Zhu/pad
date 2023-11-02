def solution():
    annual_income = 60000  # Dorothy earns $60000 a year
    tax_rate = 0.18  # Dorothy needs to pay 18% of her income in taxes

    # Calculate the amount of taxes Dorothy needs to pay
    taxes = annual_income * tax_rate

    # Calculate the amount of money Dorothy will have left after paying taxes
    money_after_taxes = annual_income - taxes
    result = money_after_taxes
    return result

print(solution())