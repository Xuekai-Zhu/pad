def solution():
    # Calculate total area that can be colored with one full marker
    total_area = 3 * (4*4) # 48 sq inches

    # Calculate area of two 6x2 rectangles
    rectangle_area = 2 * (6*2) # 24 sq inches

    # Calculate the remaining area that can still be colored
    remaining_area = total_area - rectangle_area

    # Calculate percentage of ink remaining
    ink_remaining = (remaining_area / total_area) * 100
    result = ink_remaining
    return result

print(solution())