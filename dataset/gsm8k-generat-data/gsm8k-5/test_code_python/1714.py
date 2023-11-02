def solution():
    first_warehouse_boxes = 400  # the first warehouse has 400 boxes
    second_warehouse_boxes = first_warehouse_boxes / 2  # the first warehouse has twice as many boxes as the second warehouse
    total_boxes = first_warehouse_boxes + second_warehouse_boxes  # find the total number of boxes in both warehouses combined
    result = total_boxes
    return result

print(solution())