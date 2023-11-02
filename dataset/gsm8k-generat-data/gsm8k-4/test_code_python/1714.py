def solution():
    """There are two warehouses. The first warehouse has twice as many boxes as the second warehouse. If the first warehouse has 400 boxes, how many boxes are there in both warehouses combined?"""
    # Calculate the number of boxes in the second warehouse
    second_warehouse_boxes = 400 / 2

    # Calculate the total number of boxes in both warehouses
    total_boxes = 400 + second_warehouse_boxes

    result = total_boxes
    return result

print(solution())