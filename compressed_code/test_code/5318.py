def solution():
    
    monthly_fee = 30
    first_month_fee = monthly_fee / 3
    fourth_month_fee = monthly_fee + 15
    total_fee = first_month_fee + monthly_fee + monthly_fee + fourth_month_fee + monthly_fee + monthly_fee
    result = total_fee
    return result

print(solution())