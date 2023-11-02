def solution():
    """There are two warehouses. The first warehouse has twice as many boxes as the second warehouse. If the first warehouse has 400 boxes, how many boxes are there in both warehouses combined?"""
    first_warehouse_boxes = 400
    second_warehouse_boxes = first_warehouse_boxes / 2
    total_boxes = first_warehouse_boxes + second_warehouse_boxes
    result = total_boxes
    return result

print(solution())