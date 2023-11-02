def solution():
    
    guest_count = 20
    initial_price = 25 * guest_count
    repeat_discount = 0.1
    repeat_price = initial_price - (initial_price * repeat_discount)
    result = repeat_price
    return result

print(solution())