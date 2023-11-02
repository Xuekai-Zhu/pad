def solution():
    boxes_sold_saturday = 60  # Tanika sold 60 boxes on Saturday
    boxes_sold_sunday = boxes_sold_saturday * 1.5  # Tanika sold 50% more on Sunday
    total_boxes_sold = boxes_sold_saturday + boxes_sold_sunday  # Total boxes sold over two days

    result = total_boxes_sold
    return result

print(solution())