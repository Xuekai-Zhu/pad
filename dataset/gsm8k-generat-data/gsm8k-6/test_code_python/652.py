def solution():
    # Calculate the total number of boxes sold by Tanika over the two days
    boxes_sold_on_sunday = 60 * 1.5  # she sold 50% more on Sunday than on Saturday
    total_boxes_sold = 60 + boxes_sold_on_sunday
    result = total_boxes_sold
    return result

print(solution())