def solution():
    
    first_four_months_total = 30 * 4
    last_two_months_total = 24 * 2
    total_spent = first_four_months_total + last_two_months_total
    average_monthly_bill = total_spent / 6
    result = average_monthly_bill
    return result

print(solution())