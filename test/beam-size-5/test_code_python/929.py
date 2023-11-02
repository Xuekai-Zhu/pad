def solution():
    # Calculate the total number of boxes donated
    total_boxes_donated = 10 * 5

    # Calculate the total number of boxes remaining
    total_boxes_remaining = 10 + 10

    # Calculate the total number of boxes that can fit in all the boxes
    total_boxes_remaining = total_boxes_remaining * 2

    # Calculate the number of new tables needed
    new_tables_needed = total_boxes_remaining // 15
    if total_boxes_remaining % 15!= 0:
        new_tables_needed += 1

    result = new_tables_needed
    return result

print(solution())