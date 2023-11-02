def solution():
    boxes_per_harvest = 20  # Betty gets an average of 20 boxes each harvest
    boxes_full = int(boxes_per_harvest * 0.75)  # Three-quarters of the boxes are full
    boxes_half_full = boxes_per_harvest - boxes_full  # The remaining boxes are half-full
    parsnips_per_box_full = 20  # Each full box holds 20 parsnips
    parsnips_per_box_half_full = 10  # Each half-full box holds 10 parsnips

    # Calculate the total number of parsnips in full boxes
    total_parsnips_full = boxes_full * parsnips_per_box_full

    # Calculate the total number of parsnips in half-full boxes
    total_parsnips_half_full = boxes_half_full * parsnips_per_box_half_full

    # Calculate the total number of parsnips in an average harvest
    total_parsnips = total_parsnips_full + total_parsnips_half_full
    result = total_parsnips
    return result

print(solution())