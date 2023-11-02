def solution():
    old_orange_price = 40
    new_orange_price = old_orange_price * 1.15
    old_mango_price = 50
    new_mango_price = old_mango_price * 1.15
    total_price = (new_orange_price * 10) + (new_mango_price * 10)
    result = total_price
    return result

print(solution())