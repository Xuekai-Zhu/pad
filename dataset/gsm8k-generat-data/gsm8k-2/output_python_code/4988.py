def solution():
    """Edmund owns a gift wrapping shop, he uses 18 inches of gift wrapper per gift box. If Edmund has 90 inches of gift wrapper per day, how many gift boxes will he be able to wrap every 3 days?"""
    gift_wrapper_per_day = 90
    gift_wrapper_per_box = 18
    gift_boxes_per_day = gift_wrapper_per_day // gift_wrapper_per_box
    
    gift_boxes_per_3_days = 3 * gift_boxes_per_day
    
    result = gift_boxes_per_3_days
    return result

print(solution())