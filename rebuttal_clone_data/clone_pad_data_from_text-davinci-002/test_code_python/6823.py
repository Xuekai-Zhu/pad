def solution():
    markers_in_classroom = 32
    markers_in_new_boxes = 9
    total_markers = 86
    new_boxes = total_markers - markers_in_classroom
    result = new_boxes / markers_in_new_boxes
    return result

print(solution())