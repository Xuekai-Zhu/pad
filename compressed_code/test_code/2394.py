def solution():
    
    box_size = 10
    num_boxes = 5
    sell_price = 1.5
    cost_price = 1
    total_sell_price = box_size * num_boxes * sell_price
    total_cost_price = box_size * num_boxes * cost_price
    profit = total_sell_price - total_cost_price
    result = profit
    return result

print(solution())