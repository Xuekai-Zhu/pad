def solution():
    
    cookies_per_bag = 7
    cookies_per_box = 12
    bags = 9
    boxes = 8
    
    total_cookies_in_bags = cookies_per_bag * bags
    total_cookies_in_boxes = cookies_per_box * boxes
    difference = total_cookies_in_boxes - total_cookies_in_bags
    
    result = difference
    return result

print(solution())