def solution():
    
    pencil_price = 4
    pen_price = 5
    pencil_amount = 15 * 80
    pen_amount = 300 + 2 * pencil_amount
    total_amount = pencil_amount * pencil_price + pen_amount * pen_price
    result = total_amount
    return result

print(solution())