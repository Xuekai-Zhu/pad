def solution():
    # Calculate the number of boxes used by Ali
    ali_boxes = 8 * 5

    # Calculate the remaining boxes
    remaining_boxes = 80 - ali_boxes

    # Calculate the number of circles Ernie can make
    ernie_circles = remaining_boxes // 10
    result = ernie_circles
    return result

print(solution())