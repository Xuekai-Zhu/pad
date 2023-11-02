def solution():
    
    eraser_pencil_price = 0.8
    regular_pencil_price = 0.5
    short_pencil_price = 0.4
    eraser_pencils_sold = 200
    regular_pencils_sold = 40
    short_pencils_sold = 35
    total_money_made = eraser_pencil_price * eraser_pencils_sold + regular_pencil_price * regular_pencils_sold + short_pencil_price * short_pencils_sold
    result = total_money_made
    return result

print(solution())