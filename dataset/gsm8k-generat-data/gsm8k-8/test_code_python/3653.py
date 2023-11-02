def solution():
    # Define the number of boxes and decorations per box
    num_boxes = 4
    decorations_per_box = 15

    # Calculate the total number of decorations
    total_decorations = num_boxes * decorations_per_box

    # Calculate the number of decorations Mrs. Jackson did not use
    unused_decorations = total_decorations - 35

    # Calculate the number of decorations she gave to her neighbor
    given_decorations = unused_decorations

    result = given_decorations
    return result

print(solution())