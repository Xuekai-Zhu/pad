def solution():
    # Calculate the number of blue pencils
    blue_pencils = 2 * 20

    # Calculate the total number of pencils
    total_pencils = 20 + blue_pencils + 40 + (20 + blue_pencils)

    # Calculate the total number of boxes needed
    total_boxes = total_pencils // 20

    result = total_boxes
    return result

print(solution())