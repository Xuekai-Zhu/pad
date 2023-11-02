def solution():
    
    boxes_per_week = 10
    apples_per_box = 300
    total_stock = boxes_per_week * apples_per_box
    sold_stock = 0.75 * total_stock
    unsold_stock = total_stock - sold_stock
    result = unsold_stock
    return result

print(solution())