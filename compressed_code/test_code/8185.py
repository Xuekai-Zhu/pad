def solution():
    
    new_house_cost = 500000
    loan_percent = 75
    down_payment_percent = 100 - loan_percent
    old_house_increase = 25
    old_house_cost = new_house_cost * (down_payment_percent / 100) / (1 + old_house_increase / 100)
    result = old_house_cost
    return result

print(solution())