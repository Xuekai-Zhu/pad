def solution():
    # Calculate the maximum number of boxes that can be shipped on each delivery
    weight_limit = 2000  # pounds
    light_box_weight = 10  # pounds
    heavy_box_weight = 40  # pounds
    max_boxes = weight_limit // (light_box_weight + heavy_box_weight)  # integer division
    result = max_boxes
    return result

print(solution())