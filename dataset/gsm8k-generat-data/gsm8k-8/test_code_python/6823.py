def solution():
    initial_markers = 32
    total_markers = 86
    markers_bought = total_markers - initial_markers
    boxes_bought = markers_bought // 9
    result = boxes_bought
    return result

print(solution())