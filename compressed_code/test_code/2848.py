def solution():
    
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