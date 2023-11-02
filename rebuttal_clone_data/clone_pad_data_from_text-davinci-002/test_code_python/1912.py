def solution():
    total_weight = 2000
    light_weight = 10
    heavy_weight = 40
    light_boxes = total_weight / light_weight
    heavy_boxes = total_weight / heavy_weight
    total_boxes = light_boxes + heavy_boxes
    boxes_per_truck = total_boxes / 3
    result = boxes_per_truck
   
    return result

print(solution())