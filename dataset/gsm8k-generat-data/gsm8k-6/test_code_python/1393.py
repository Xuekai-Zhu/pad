def solution():
    # Calculate total number of jars packed in each scenario
    jars_in_ten_boxes = 12 * 10  # 12 jars in 10 boxes
    jars_in_thirty_boxes = 10 * 30  # 10 jars in 30 boxes
    
    # Calculate total number of boxes needed for all jars
    total_boxes_needed = (500 // 12) + (500 // 10)  # integer division to round down sides
    
    # Calculate total number of jars packed in all boxes
    total_jars_packed = jars_in_ten_boxes + jars_in_thirty_boxes * (total_boxes_needed - 10)
    
    # Calculate number of jars left
    jars_left = 500 - total_jars_packed
    
    result = jars_left
    return result

print(solution())