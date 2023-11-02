def solution():
    # Calculate the number of boxes used by Ali and Ernie
    ali_boxes = 8 * 5  # Ali made 5 circles with 8 boxes each
    ernie_boxes = 80 - ali_boxes  # Remaining boxes for Ernie to use

    # Calculate the number of circles Ernie can make with the remaining boxes
    ernie_circles = ernie_boxes // 10
    result = ernie_circles
    return result

print(solution())