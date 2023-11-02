def solution():
    
    shoes_price = 74
    socks_price = 2 * 2
    bag_price = 42
    total_price = shoes_price + socks_price + bag_price
    discount_threshold = 100

    if total_price > discount_threshold:
        discount_amount = 0.1 * (total_price - discount_threshold)
        total_price -= discount_amount

    result = total_price
    return result

print(solution())