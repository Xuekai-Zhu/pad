def solution():
    
    base_pay = 12.00
    num_customers = 20
    tip_amount = 1.25
    total_tips = num_customers * tip_amount
    total_earnings = base_pay + total_tips
    result = total_earnings
    return result

print(solution())