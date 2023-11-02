def solution():
    small_boxes = 2400
    medium_boxes = 1800
    hugo_small_time = 3
    hugo_medium_time = 2 * hugo_small_time
    tom_small_time = 4
    tom_medium_time = tom_small_time
    
    hugo_total_time = (small_boxes * hugo_small_time) + (medium_boxes * hugo_medium_time)
    tom_total_time = (small_boxes * tom_small_time) + (medium_boxes * tom_medium_time)
    
    if hugo_total_time < tom_total_time:
        result = hugo_total_time
    else:
        result = tom_total_time
    
    return result

print(solution())