def solution():
    children = 3  # Peyton has 3 children
    juice_boxes_per_child_per_day = 1  # Each child gets 1 juice box per day
    days_per_week = 5  # The children get juice boxes 5 days per week
    weeks = 25  # The school year is 25 weeks long

    # Calculate the total number of juice boxes needed for the entire school year
    total_juice_boxes = children * juice_boxes_per_child_per_day * days_per_week * weeks
    result = total_juice_boxes
    return result

print(solution())