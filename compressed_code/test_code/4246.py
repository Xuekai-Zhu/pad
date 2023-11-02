def solution():
    
    set_price = 2000
    gift_cards = 200
    discounted_price = set_price * 0.85
    credit_card_discount = discounted_price * 0.1
    final_price = discounted_price - credit_card_discount - gift_cards
    result = final_price
    return result

print(solution())