def solution():
    """Peyton has 3 children and they each get a juice box in their lunch, 5 days a week. The school year is 25 weeks long. How many juices boxes will she need for the entire school year for all of her children?"""
    num_children = 3
    juice_boxes_per_child_per_week = 5
    weeks_per_school_year = 25
    total_juice_boxes = num_children * juice_boxes_per_child_per_week * weeks_per_school_year
    result = total_juice_boxes
    return result

print(solution())