def solution():
    jars_per_box_1 = 12
    boxes_1 = 10
    jars_per_box_2 = 10
    boxes_2 = 30
    total_jars = 500

    # Calculate the total number of jars in the first set of boxes
    total_jars_1 = jars_per_box_1 * boxes_1

    # Calculate the total number of jars in the second set of boxes
    total_jars_2 = jars_per_box_2 * boxes_2

    # Calculate the total number of jars that can fit in all the boxes
    total_jars_boxes = total_jars_1 + total_jars_2

    # Calculate the number of jars left after all the boxes are full
    jars_left = total_jars - total_jars_boxes
    result = jars_left
    return result

print(solution())