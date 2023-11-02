def solution():
    # Calculate the number of jars in each box for the first scenario
    jars_per_box_1 = 12 / 10

    # Calculate the total number of boxes in the first scenario
    total_boxes_1 = 500 / jars_per_box_1

    # Calculate the number of jars left after filling all the boxes in the first scenario
    jars_left_1 = 500 - (int(total_boxes_1) * 12)

    # Calculate the number of jars in each box for the second scenario
    jars_per_box_2 = 10 / 30

    # Calculate the total number of boxes in the second scenario
    total_boxes_2 = 500 / jars_per_box_2

    # Calculate the number of jars left after filling all the boxes in the second scenario
    jars_left_2 = 500 - (int(total_boxes_2) * 10)

    # Take the minimum of the two jars left scenarios
    jars_left = min(jars_left_1, jars_left_2)

    result = jars_left
    return result

print(solution())