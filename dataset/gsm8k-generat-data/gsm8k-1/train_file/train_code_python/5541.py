def solution():
    """Betty is growing parsnips in her vegetable garden. When the parsnips are grown, they are harvested and bundled into boxes that can hold up to 20 parsnips each. Each harvest, three-quarters of the boxes are full, and the remaining boxes are half-full. She gets an average of 20 boxes each harvest. How many parsnips does Betty grow in an average harvest?"""
    boxes_per_harvest = 20
    full_boxes = int(boxes_per_harvest * 0.75)
    half_full_boxes = boxes_per_harvest - full_boxes
    full_box_capacity = 20
    half_full_box_capacity = 10
    total_parsnips = (full_boxes * full_box_capacity) + (half_full_boxes * half_full_box_capacity)
    result = total_parsnips
    return result

print(solution())