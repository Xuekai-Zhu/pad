def solution():
    # Find the area of the living room
    area = 16 * 20

    # Find the remaining area to cover
    remaining_area = area - 250

    # Find the number of boxes needed to cover the remaining area
    boxes_needed = remaining_area / 10

    # Round up the number of boxes to account for partial boxes
    boxes_needed = math.ceil(boxes_needed)

    result = boxes_needed
    return result

print(solution())