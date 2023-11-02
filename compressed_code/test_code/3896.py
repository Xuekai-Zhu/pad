def solution():
    
    initial_investment = 300
    monthly_interest_rate = 0.1
    first_month_total = initial_investment + (initial_investment * monthly_interest_rate)
    second_month_total = first_month_total + (first_month_total * monthly_interest_rate)
    total_amount = round(second_month_total, 2)
    result = total_amount
    return result

print(solution())