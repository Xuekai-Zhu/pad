def solution():
    
    doughnuts_per_box = 10
    total_doughnuts = 300
    sold_boxes = 27
    sold_doughnuts = sold_boxes * doughnuts_per_box
    left_doughnuts = total_doughnuts - sold_doughnuts
    result = left_doughnuts
    return result

print(solution())