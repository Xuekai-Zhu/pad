def solution():
    """Henry drinks 15 bottles of kombucha every month. Each bottle costs $3.00 and is eligible for a cash refund of $0.10 per bottle when he takes it to a recycling center. After 1 year, how many bottles of kombucha will he be able to buy after he receives his cash refund?"""
    bottles_per_month = 15
    price_per_bottle = 3.00
    cash_refund_per_bottle = 0.10
    total_bottles = bottles_per_month * 12
    cash_refund_total = total_bottles * cash_refund_per_bottle
    total_cost = total_bottles * price_per_bottle
    bottles_after_cash_refund = (total_cost - cash_refund_total) / price_per_bottle
    result = bottles_after_cash_refund
    return result

print(solution())