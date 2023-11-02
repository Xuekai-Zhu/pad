def solution():
    # Calculate the total area of the marker's ink
    total_area = 3 * (4*4)  # each square is 4x4 inches

    # Calculate the area of the two rectangles
    rectangle_area = 2 * (6*2)

    # Calculate the remaining ink in percentage
    remaining_area = total_area - rectangle_area
    remaining_percentage = (remaining_area / total_area) * 100
    result = remaining_percentage
    return result

print(solution())