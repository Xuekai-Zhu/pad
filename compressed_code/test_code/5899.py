def solution():
    
    lottery_winnings = 50
    tax_percent = 20
    processing_fee = 5
    tax_amount = lottery_winnings * (tax_percent / 100)
    amount_after_tax = lottery_winnings - tax_amount
    amount_after_processing_fee = amount_after_tax - processing_fee
    result = amount_after_processing_fee
    return result

print(solution())