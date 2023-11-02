def solution():
    
    total_apples = 10000
    apples_per_box = 50
    boxes = total_apples // apples_per_box
    box_price = 35
    total_earnings = boxes * box_price
    result = total_earnings
    return result

print(solution())