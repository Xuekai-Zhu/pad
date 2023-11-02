def solution():
    """Loisa wants to buy a tablet that costs $450 cash. Since she does not have enough money, the store offered her an installment plan for 12 months. She will pay $100 as a down payment and pay $40 for the first 4 months; then $35 for the next four months; then $30 for the last four months. How much will Loisa save if she will buy the tablet in cash instead of on installment?"""
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