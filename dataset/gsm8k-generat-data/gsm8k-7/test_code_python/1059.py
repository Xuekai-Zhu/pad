def solution():
    num_children = 3
    num_juice_boxes_per_child_per_week = 5
    num_weeks = 25

    # Calculate the total number of juice boxes needed for one child for the entire school year
    total_juice_boxes_per_child = num_juice_boxes_per_child_per_week * num_weeks

    # Calculate the total number of juice boxes needed for all of Peyton's children for the entire school year
    total_juice_boxes = total_juice_boxes_per_child * num_children
    result = total_juice_boxes
    return result

print(solution())