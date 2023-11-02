def solution():
    
    boxes = 48
    erasers_per_box = 24
    eraser_price = 0.75
    total_erasers = boxes * erasers_per_box
    total_money = total_erasers * eraser_price
    result = total_money
    return result

print(solution())