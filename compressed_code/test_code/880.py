def solution():
    
    shoes_price = 200
    shoes_discount = 0.3
    shoes_discounted_price = shoes_price * (1 - shoes_discount)
    shirts_price = 80
    number_of_shirts = 2
    shirts_full_price = shirts_price * number_of_shirts
    discount = 0.05
    total_price = shoes_discounted_price + shirts_full_price
    total_discount = total_price * discount
    final_price = total_price - total_discount
    result = final_price
    return result

print(solution())