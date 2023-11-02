def solution():
    num_boxes_weekdays = 3
    num_boxes_saturday = num_boxes_weekdays * 2
    num_boxes_sunday = num_boxes_weekdays * 3

    total_boxes_per_week = (num_boxes_weekdays * 5) + num_boxes_saturday + num_boxes_sunday
    result = total_boxes_per_week
    return result

print(solution())