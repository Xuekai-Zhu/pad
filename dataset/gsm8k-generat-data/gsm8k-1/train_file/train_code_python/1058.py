def solution():
    """Peyton has 3 children and they each get a juice box in their lunch, 5 days a week. The school year is 25 weeks long. How many juice boxes will she need for the entire school year for all of her children?"""
    children = 3
    days_per_week = 5
    weeks_per_school_year = 25
    juice_boxes_per_child = children * days_per_week
    juice_boxes_total = juice_boxes_per_child * weeks_per_school_year
    result = juice_boxes_total
    return result

print(solution())