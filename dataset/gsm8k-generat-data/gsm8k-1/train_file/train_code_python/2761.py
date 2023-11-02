def solution():
    """Henry drinks 15 bottles of kombucha every month. Each bottle costs $3.00 and is eligible for a cash refund of $0.10 per bottle when he takes it to a recycling center. After 1 year, how many bottles of kombucha will he be able to buy after he receives his cash refund?"""
    bottles_per_month = 15
    cost_per_bottle = 3.00
    refund_per_bottle = 0.10
    total_refund_per_month = bottles_per_month * refund_per_bottle
    total_cost_per_month = bottles_per_month * cost_per_bottle
    bottles_bought_per_month = (total_cost_per_month - total_refund_per_month) / cost_per_bottle
    bottles_bought_per_year = bottles_bought_per_month * 12
    result = bottles_bought_per_year
    return result

print(solution())