def solution():
    """George wants to borrow $100 from a loan shark. The finance fee starts at 5% and doubles every week. If George plans to borrow for 2 weeks, how much in fees will he have to pay?"""
    amount_borrowed = 100
    weeks_borrowed = 2
    total_fees = 0
    current_fee_rate = 0.05
    for i in range(weeks_borrowed):
        fees_for_week = amount_borrowed * current_fee_rate
        total_fees += fees_for_week
        current_fee_rate *= 2

    result = total_fees
    return result

print(solution())