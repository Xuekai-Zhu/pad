def solution():
    """Betty is growing parsnips in her vegetable garden. When the parsnips are grown, they are harvested and bundled into boxes that can hold up to 20 parsnips each. Each harvest, three-quarters of the boxes are full, and the remaining boxes are half-full. She gets an average of 20 boxes each harvest. How many parsnips does Betty grow in an average harvest?"""
    box_capacity = 20
    full_boxes_percentage = 0.75
    half_boxes_percentage = 0.25
    total_boxes = 20
    full_boxes = total_boxes * full_boxes_percentage
    half_boxes = total_boxes * half_boxes_percentage
    total_parsnips = (full_boxes * box_capacity) + (half_boxes * (box_capacity/2))
    result = total_parsnips
    return result

print(solution())