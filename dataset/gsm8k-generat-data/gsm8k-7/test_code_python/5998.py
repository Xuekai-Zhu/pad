def solution():
    total_boxes = 80
    ali_circles = 5
    ali_boxes = 8
    ernie_boxes = 10

    # Calculate the total number of boxes used by Ali
    total_ali_boxes = ali_circles * ali_boxes

    # Calculate the remaining boxes
    remaining_boxes = total_boxes - total_ali_boxes

    # Calculate the number of circles Ernie can make
    ernie_circles = remaining_boxes / ernie_boxes
    result = ernie_circles
    return result

print(solution())