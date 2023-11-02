def solution():
    
    starting_markers = 32
    total_markers = 86
    markers_bought = total_markers - starting_markers
    markers_per_box = 9
    boxes_bought = markers_bought // markers_per_box
    result = boxes_bought
    return result

print(solution())