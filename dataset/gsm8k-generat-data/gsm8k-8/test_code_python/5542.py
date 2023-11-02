def solution():
    # Define the variables
    full_boxes = 0.75 * 20
    half_boxes = 0.25 * 20
    total_boxes = 20
    parsnips_per_box = 20

    # Calculate the total number of parsnips
    total_parsnips = (full_boxes * parsnips_per_box) + (half_boxes * parsnips_per_box * 0.5)

    # Calculate the average number of parsnips per harvest
    avg_parsnips = total_parsnips / total_boxes
    result = avg_parsnips
    return result

print(solution())