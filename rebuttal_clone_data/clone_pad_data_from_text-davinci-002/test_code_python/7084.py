def solution():
    total_boxes_sold = 150
    percent_increase = 50
    boxes_sold_on_sunday = total_boxes_sold - (total_boxes_sold / (100 + percent_increase))
    boxes_sold_on_saturday = total_boxes_sold - boxes_sold_on_sunday
    result = boxes_sold_on_saturday
    return result

print(solution())