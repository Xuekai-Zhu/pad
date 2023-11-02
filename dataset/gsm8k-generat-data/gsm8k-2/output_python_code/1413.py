def solution():
    """Stacy just bought a 6 month prescription of flea & tick medicine for her dog for $150.00 online. Her cashback app was offering 10% cashback and she has a mail-in rebate for $25.00 on a 6-month prescription. How much will the medicine cost after cash back and rebate offers?"""
    original_price = 150
    cashback_percent = 0.1
    mail_in_rebate = 25
    cashback_amount = original_price * cashback_percent
    discounted_price = original_price - mail_in_rebate - cashback_amount
    result = discounted_price
    return result

print(solution())