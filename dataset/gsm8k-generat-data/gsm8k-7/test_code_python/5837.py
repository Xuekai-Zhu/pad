def solution():
    shirt_boxes_per_roll = 5
    xl_boxes_per_roll = 3
    num_shirt_boxes = 20
    num_xl_boxes = 12
    cost_per_roll = 4.0

    # Calculate the number of rolls of wrapping paper needed for the shirt boxes
    num_shirt_rolls = num_shirt_boxes // shirt_boxes_per_roll
    if num_shirt_boxes % shirt_boxes_per_roll != 0:
        num_shirt_rolls += 1

    # Calculate the number of rolls of wrapping paper needed for the XL boxes
    num_xl_rolls = num_xl_boxes // xl_boxes_per_roll
    if num_xl_boxes % xl_boxes_per_roll != 0:
        num_xl_rolls += 1

    # Calculate the total number of rolls of wrapping paper needed
    total_rolls = num_shirt_rolls + num_xl_rolls

    # Calculate the total cost of all rolls of wrapping paper needed
    total_cost = total_rolls * cost_per_roll
    result = total_cost
    return result

print(solution())