def solution():
    # Calculate the number of full boxes and half-full boxes in an average harvest
    full_boxes = 0.75 * 20  # 75% of the boxes are full
    half_full_boxes = 0.25 * 20  # 25% of the boxes are half-full

    # Calculate the total number of parsnips in an average harvest
    total_parsnips = full_boxes * 20 + half_full_boxes * 10  # full boxes contain 20 parsnips each, half-full boxes contain 10 parsnips each
    result = total_parsnips
    return result

print(solution())