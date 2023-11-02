def solution():
    # Calculate the total area of the living room
    living_room_area = 16 * 20

    # Subtract the area already covered from the total area
    remaining_area = living_room_area - 250

    # Calculate the number of boxes needed to cover the remaining area
    boxes_needed = remaining_area / 10

    # Round up to the nearest whole number of boxes
    boxes_needed = math.ceil(boxes_needed)

    result = boxes_needed
    return result

print(solution())