def solution():
    
    canvas_price = 40
    paint_price = 0.5 * canvas_price
    easel_price = 15
    total_spent = 90
    total_spent -= easel_price  
    total_spent -= canvas_price  
    total_spent -= paint_price  
    result = total_spent
    return result

print(solution())