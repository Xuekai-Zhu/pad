def solution():
    
    children = 3
    days_per_week = 5
    weeks_per_school_year = 25
    juice_boxes_per_child = children * days_per_week
    juice_boxes_total = juice_boxes_per_child * weeks_per_school_year
    result = juice_boxes_total
    return result

print(solution())