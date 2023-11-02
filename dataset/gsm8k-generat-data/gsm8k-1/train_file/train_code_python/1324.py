def solution():
    """Sally earned $1000 at work last month. This month, she received a 10% raise. How much money will she make in total for the two months?"""
    monthly_pay = 1000
    raise_percent = 10
    total_pay = (monthly_pay * 2) + (monthly_pay * (raise_percent / 100))
    result = total_pay
    return result

print(solution())