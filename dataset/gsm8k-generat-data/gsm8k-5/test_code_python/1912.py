def solution():
    max_load = 2000  # Maximum load capacity of each truck is 2000 pounds
    lighter_box_weight = 10  # Weight of each lighter box is 10 pounds
    heavier_box_weight = 40  # Weight of each heavier box is 40 pounds
    num_trucks = 3  # Steven has 3 trucks available for each delivery

    # Calculate the number of lighter boxes that can be shipped in each delivery
    lighter_boxes_per_delivery = max_load // lighter_box_weight // num_trucks
    # Calculate the number of heavier boxes that can be shipped in each delivery
    heavier_boxes_per_delivery = max_load // heavier_box_weight // num_trucks
    # Calculate the total number of boxes that can be shipped in each delivery
    total_boxes_per_delivery = lighter_boxes_per_delivery + heavier_boxes_per_delivery
    result = total_boxes_per_delivery
    return result

print(solution())