def solution():
    red_pencils = 20
    blue_pencils = 2 * red_pencils
    yellow_pencils = 40
    green_pencils = red_pencils + blue_pencils

    total_pencils = red_pencils + blue_pencils + yellow_pencils + green_pencils

    total_boxes = total_pencils // 20

    result = total_boxes
    return result

print(solution())