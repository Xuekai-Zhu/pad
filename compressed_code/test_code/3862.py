def solution():
    
    lollipop_price = 1.5
    gummy_price = 2
    lollipop_quantity = 4
    gummy_quantity = 2
    total_price = (lollipop_price * lollipop_quantity) + (gummy_price * gummy_quantity)
    remaining_money = 15 - total_price
    result = remaining_money
    return result

print(solution())