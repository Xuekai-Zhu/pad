def solution():
    
    cookies_per_box = 48
    boxes_collected_by_abigail = 2
    boxes_collected_by_grayson = 3/4
    boxes_collected_by_olivia = 3
    total_boxes = boxes_collected_by_abigail + boxes_collected_by_grayson + boxes_collected_by_olivia
    total_cookies = total_boxes * cookies_per_box
    result = total_cookies
    
    return result

print(solution())