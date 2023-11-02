def solution():
    
    pot_price = 120
    mixing_bowl_price = 20
    utensils_price = 5
    discount = 0.2
    total_price = pot_price + mixing_bowl_price + utensils_price
    discounted_price = total_price * (1 - discount)
    result = discounted_price
    return result

print(solution())