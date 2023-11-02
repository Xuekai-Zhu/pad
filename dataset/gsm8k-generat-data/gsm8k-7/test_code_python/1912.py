def solution():
    truck_capacity = 2000
    lighter_box_weight = 10
    heavier_box_weight = 40

    # Calculate the maximum number of light boxes that can fit in a truck
    max_light_boxes = truck_capacity // lighter_box_weight

    # Calculate the maximum number of heavy boxes that can fit in a truck
    max_heavy_boxes = truck_capacity // heavier_box_weight

    # Calculate the total weight of one delivery
    delivery_weight = truck_capacity * 3

    # Calculate the maximum number of light boxes and heavy boxes that can fit in one delivery
    max_light_boxes_per_delivery = max_light_boxes * 3
    max_heavy_boxes_per_delivery = max_heavy_boxes * 3

    # Find the minimum number of boxes that can fill a complete delivery
    min_boxes_per_delivery = min(max_light_boxes_per_delivery, max_heavy_boxes_per_delivery)

    # Divide the delivery weight by the weight of one box to find the maximum number of boxes that can be shipped in one delivery
    max_boxes_per_delivery = delivery_weight // (lighter_box_weight + heavier_box_weight)

    # Find the minimum of the two values
    max_boxes_per_delivery = min(min_boxes_per_delivery, max_boxes_per_delivery)

    result = max_boxes_per_delivery
    return result

print(solution())