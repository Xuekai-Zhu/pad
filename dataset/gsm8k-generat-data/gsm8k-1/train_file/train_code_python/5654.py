def solution():
    """Lolita can drink 3 boxes of milk during weekdays. During Saturdays, she can drink twice the number of boxes of milk than on the weekdays, and during Sundays, she can drink thrice the number of boxes of milk than on the weekdays. How many boxes of milk does she drink per week?"""
    weekday_boxes = 3
    saturday_boxes = 2 * weekday_boxes
    sunday_boxes = 3 * weekday_boxes
    total_boxes = (weekday_boxes * 5) + saturday_boxes + sunday_boxes
    result = total_boxes
    return result

print(solution())