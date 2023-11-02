def solution():
    
    house_price = 100000
    down_payment_percent = 20
    down_payment = house_price * (down_payment_percent / 100)
    remaining_balance = house_price - down_payment
    parents_payment_percent = 30
    parents_payment = remaining_balance * (parents_payment_percent / 100)
    balance_after_parents_payment = remaining_balance - parents_payment
    result = balance_after_parents_payment
    return result

print(solution())