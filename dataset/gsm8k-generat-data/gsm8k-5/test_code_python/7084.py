def solution():
    total_boxes_sold = 150  # Sally sold a total of 150 boxes on Saturday and Sunday
    sunday_boxes_sold = 1.5 * saturday_boxes_sold  # Sally sold 50% more on Sunday than on Saturday

    # Use algebra to solve for the number of boxes sold on Saturday
    # saturday_boxes_sold + sunday_boxes_sold = total_boxes_sold
    # saturday_boxes_sold + 1.5 * saturday_boxes_sold = 150
    # 2.5 * saturday_boxes_sold = 150
    # saturday_boxes_sold = 60

    saturday_boxes_sold = total_boxes_sold / 2.5
    result = saturday_boxes_sold
    return result

print(solution())