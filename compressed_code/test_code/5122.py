def solution():
    
    pants_price = 110
    socks_price = 60
    pants_discount = 0.3
    socks_discount = 0.3
    total_pants_price = pants_price * 4 * (1 - pants_discount)
    total_socks_price = socks_price * 2 * (1 - socks_discount)
    total_price = total_pants_price + total_socks_price
    result = total_price
    return result

print(solution())