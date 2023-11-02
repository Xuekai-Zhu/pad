def solution():
    months_to_pay_back = 11
    monthly_payment = 15
    additional_percentage = 10
    money_borrowed = monthly_payment / ((additional_percentage / 100) + 1)
    total_money_repaid = monthly_payment * months_to_pay_back
    result = total_money_repaid - money_borrowed
    return result

print(solution())