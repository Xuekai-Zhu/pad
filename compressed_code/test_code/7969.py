def solution():
    
    pen_price = 0.15
    pencil_price = 0.25
    num_pens = 40
    num_pencils = int(num_pens * (2/5 + 1))
    total_spent = num_pens * pen_price + num_pencils * pencil_price
    result = total_spent
    return result

print(solution())