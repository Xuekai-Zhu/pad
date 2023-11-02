def solution():
    original_price = 150.0
    cashback_percent = 0.1
    mail_in_rebate = 25.0

    # Calculate the cash back amount
    cashback_amount = original_price * cashback_percent

    # Subtract the cash back amount and the mail-in rebate from the original price
    total_cost = original_price - cashback_amount - mail_in_rebate
    result = total_cost
    return result

print(solution())