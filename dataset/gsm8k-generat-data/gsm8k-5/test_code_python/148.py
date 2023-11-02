def solution():
    winnings = 50  # Winwin won $50
    tax = 0.2 * winnings  # 20% of her winnings went to tax
    processing_fee = 5  # She paid $5 for processing fee

    # Calculate the amount Winwin was able to take home
    take_home_amount = winnings - tax - processing_fee
    result = take_home_amount
    return result

print(solution())