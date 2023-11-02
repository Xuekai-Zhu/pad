def solution():
    ali_boxes = 8  # Ali used 8 boxes to make each of his circles
    ernie_boxes = 10  # Ernie used 10 boxes to make each of his circles
    total_boxes = 80  # They had 80 boxes to begin with
    ali_circles = 5  # Ali made 5 circles

    # Calculate the number of boxes Ali used
    ali_total_boxes = ali_boxes * ali_circles

    # Calculate the number of boxes Ernie has left
    ernie_boxes_left = total_boxes - ali_total_boxes

    # Calculate the number of circles Ernie can make with the boxes left
    ernie_circles = ernie_boxes_left // ernie_boxes
    result = ernie_circles
    return result

print(solution())