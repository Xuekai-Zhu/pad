def solution():
    large_box_tape = 4
    medium_box_tape = 2
    small_box_tape = 1
    label_tape = 1
    num_large_boxes = 2
    num_medium_boxes = 8
    num_small_boxes = 5

    # Calculate the total amount of tape used for all large boxes
    total_large_tape = num_large_boxes * large_box_tape

    # Calculate the total amount of tape used for all medium boxes
    total_medium_tape = num_medium_boxes * medium_box_tape

    # Calculate the total amount of tape used for all small boxes
    total_small_tape = num_small_boxes * small_box_tape

    # Calculate the total amount of tape used for all boxes
    total_box_tape = total_large_tape + total_medium_tape + total_small_tape

    # Calculate the total amount of tape used for all labels
    total_label_tape = (num_large_boxes + num_medium_boxes + num_small_boxes) * label_tape

    # Calculate the grand total of tape used for all boxes and labels
    grand_total_tape = total_box_tape + total_label_tape
    result = grand_total_tape
    return result

print(solution())