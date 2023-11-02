def solution():
    
    rooms = 5
    primer_price = 30
    primer_discount = 0.2
    paint_price = 25
    total_primer_price = rooms * primer_price * (1 - primer_discount)
    total_paint_price = rooms * paint_price
    total_cost = total_primer_price + total_paint_price
    result = total_cost
    return result

print(solution())