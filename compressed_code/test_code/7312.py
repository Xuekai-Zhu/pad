def solution():
    
    num_boxes = 10
    num_pouches_per_box = 6
    total_pouches = num_boxes * num_pouches_per_box
    total_cost = 1200  
    cost_per_pouch = total_cost // total_pouches
    result = cost_per_pouch
    return result

print(solution())