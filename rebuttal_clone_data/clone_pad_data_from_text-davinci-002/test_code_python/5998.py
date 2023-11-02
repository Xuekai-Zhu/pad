def solution():
    alis_circle = 8
    ernies_circle = 10
    total_boxes = 80
    alis_circles = 5
    ernies_circles = (total_boxes - (alis_circle * alis_circles)) / ernies_circle
    result = ernies_circles
    return result

print(solution())