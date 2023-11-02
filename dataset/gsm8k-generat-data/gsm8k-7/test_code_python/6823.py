def solution():
    initial_markers = 32
    total_markers = 86

    markers_per_box = 9

    # Calculate the number of additional markers Mr. Smith bought
    additional_markers = total_markers - initial_markers

    # Calculate the number of boxes Mr. Smith bought
    num_boxes = additional_markers / markers_per_box

    result = num_boxes
    return result

print(solution())