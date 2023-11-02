def solution():
     day_portion_1 = 0.5
     day_portion_2 = 2
     total_cookies_needed = (day_portion_1 * 2) + day_portion_2
     cookies_per_box = 45
     number_of_boxes = total_cookies_needed / cookies_per_box
     result = number_of_boxes
    
     return result

print(solution())