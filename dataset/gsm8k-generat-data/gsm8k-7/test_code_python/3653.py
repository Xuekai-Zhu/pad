def solution():
    num_boxes = 4
    decorations_per_box = 15
    decorations_used = 35

    # Calculate the total number of decorations in all boxes
    total_decorations = num_boxes * decorations_per_box

    # Calculate the number of decorations that Mrs. Jackson gave away
    decorations_given = total_decorations - decorations_used
    result = decorations_given
    return result

print(solution())