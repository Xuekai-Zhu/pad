def solution():
    
    wage_rate = 10
    tip_rate = 15
    total_wage_cost = wage_rate * 40
    total_tip_cost = tip_rate * 40
    total_cost = total_wage_cost + total_tip_cost
    downpayment_percent = 20
    downpayment_amount = (total_cost * downpayment_percent / 100) / 100
    weeks_to_save = downpayment_amount / downpayment_amount
    result = weeks_to_save
    return result

print(solution())