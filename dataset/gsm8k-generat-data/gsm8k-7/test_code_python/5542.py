def solution():
    boxes_per_harvest = 20
    full_boxes_percent = 0.75
    half_full_boxes_percent = 0.25

    # Calculate the number of full boxes and half-full boxes in an average harvest
    num_full_boxes = boxes_per_harvest * full_boxes_percent
    num_half_full_boxes = boxes_per_harvest * half_full_boxes_percent

    # Calculate the total number of parsnips in the full boxes and half-full boxes
    total_parsnips_in_full_boxes = num_full_boxes * 20
    total_parsnips_in_half_full_boxes = num_half_full_boxes * 10

    # Calculate the total number of parsnips in an average harvest
    total_parsnips = total_parsnips_in_full_boxes + total_parsnips_in_half_full_boxes
    result = total_parsnips
    return result

print(solution())