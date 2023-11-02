def solution():
    # Calculate the total area of squares the marker can color
    total_area = 3 * (4*4)  # 3 squares with 4 inch by 4 inch area

    # Calculate the area of the rectangles colored
    colored_area = 2 * (6*2)  # 2 rectangles with 6 inch by 2 inch area

    # Calculate the remaining ink in the marker
    remaining_area = total_area - colored_area

    # Calculate the percentage of ink left
    percentage_left = (remaining_area / total_area) * 100
    result = percentage_left
    return result

print(solution())