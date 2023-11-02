def solution():
    num_boxes = 12
    box_price = 9
    masks_per_box = 50
    
    repacked_boxes = 6
    repack_price = 5
    repack_size = 25
    
    baggie_price = 3
    baggie_size = 10
    
    # Calculate the total cost of all the boxes of face masks
    total_cost = num_boxes * box_price
    
    # Calculate the total revenue from selling the repacked boxes
    repack_revenue = (repacked_boxes * masks_per_box * repack_price) / (repack_size * 2)
    
    # Calculate the total revenue from selling the remaining masks in baggies
    baggie_revenue = (300 / baggie_size) * baggie_price
    
    # Calculate the total profit
    total_profit = (repack_revenue + baggie_revenue) - total_cost
    result = total_profit
    return result

print(solution())