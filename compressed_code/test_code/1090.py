def solution():
    
    original_price = 150
    cashback_percent = 0.1
    mail_in_rebate = 25
    cashback_amount = original_price * cashback_percent
    discounted_price = original_price - mail_in_rebate - cashback_amount
    result = discounted_price
    return result

print(solution())