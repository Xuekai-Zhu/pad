def solution():
    
    cookies_per_tray = 80
    boxes_per_tray = cookies_per_tray / 60
    total_boxes = boxes_per_tray * 3
    box_cost = 3.5
    total_cost = total_boxes * box_cost
    result = total_cost
    return result

print(solution())