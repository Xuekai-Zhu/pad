def solution():
    
    gift_wrapper_per_day = 90
    gift_wrapper_per_box = 18
    gift_boxes_per_day = gift_wrapper_per_day // gift_wrapper_per_box
    
    gift_boxes_per_3_days = 3 * gift_boxes_per_day
    
    result = gift_boxes_per_3_days
    return result

print(solution())