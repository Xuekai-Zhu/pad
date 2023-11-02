def solution():
    """Winwin won $50 in a lottery. She paid 20% for the tax and she paid $5 for the processing fee. How much was she able to take home?"""
    lottery_winnings = 50
    tax_percent = 20
    processing_fee = 5
    tax_amount = lottery_winnings * (tax_percent / 100)
    amount_after_tax = lottery_winnings - tax_amount
    amount_after_processing_fee = amount_after_tax - processing_fee
    result = amount_after_processing_fee
    return result

print(solution())