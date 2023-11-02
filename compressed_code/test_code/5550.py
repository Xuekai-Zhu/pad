def solution():
    
    num_colors = 4
    num_crayons_per_color = 2
    num_crayons_per_box = num_colors * num_crayons_per_color
    num_boxes_per_hour = 5
    num_crayons_per_hour = num_boxes_per_hour * num_crayons_per_box
    total_crayons = num_crayons_per_hour * 4
    result = total_crayons
    return result

print(solution())