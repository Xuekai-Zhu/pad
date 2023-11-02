def solution():
    
    cash_price = 450
    installment_down_payment = 100
    installment_payment_1 = 40
    installment_payment_2 = 35
    installment_payment_3 = 30
    installment_total = (
        installment_down_payment
        + installment_payment_1 * 4
        + installment_payment_2 * 4
        + installment_payment_3 * 4
    )
    cash_savings = installment_total - cash_price
    result = cash_savings
    return result

print(solution())