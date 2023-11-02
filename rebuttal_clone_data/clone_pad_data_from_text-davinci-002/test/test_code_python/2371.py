def solution():
    gift_card_amount = 200
    amount_spent_on_monday = gift_card_amount / 2
    amount_left = gift_card_amount - amount_spent_on_monday
    amount_spent_on_tuesday = amount_left / 4
    final_amount_left = amount_left - amount_spent_on_tuesday
    result = final_amount_left
    
    return result

print(solution())