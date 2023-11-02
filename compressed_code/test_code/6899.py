def solution():
    
    initial_cost = 150
    cashback_percent = 10
    mail_in_rebate = 25
    
    cashback_amount = initial_cost * (cashback_percent / 100)
    final_cost = initial_cost - mail_in_rebate - cashback_amount
    
    return final_cost

print(solution())