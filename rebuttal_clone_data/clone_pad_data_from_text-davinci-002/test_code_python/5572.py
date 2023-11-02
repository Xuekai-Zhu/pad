def solution():
     small_boxes = 10
     medium_boxes = 12
     total_boxes = small_boxes + medium_boxes
     large_boxes = total_boxes / 3
     total_presents = total_boxes + large_boxes
     result = total_presents
     return result

print(solution())