def solution():
    
    set_price = 2000
    gift_card = 200
    discount_1 = 0.15
    discount_2 = 0.10

    discounted_price = set_price - set_price * discount_1
    final_price = discounted_price - discounted_price * discount_2 - gift_card

    result = final_price
    return result

print(solution())