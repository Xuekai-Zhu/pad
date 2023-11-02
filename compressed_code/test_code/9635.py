def solution():
    
    boxes = 3
    masks_per_box = 20
    masks_total = boxes * masks_per_box
    sale_price = 0.5
    cost = 15
    revenue = sale_price * masks_total
    profit = revenue - cost
    result = profit
    return result

print(solution())