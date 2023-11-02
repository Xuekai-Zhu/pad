def solution():
    
    hens = 270
    roosters = 3
    total_birds = hens + roosters
    eggs_per_day = total_birds
    boxes_per_day = eggs_per_day // 6
    days_per_week = 7
    total_boxes = boxes_per_day * days_per_week
    result = total_boxes
    return result

print(solution())