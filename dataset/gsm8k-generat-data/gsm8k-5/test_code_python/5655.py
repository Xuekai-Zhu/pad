def solution():
    weekday_boxes = 3  # Lolita drinks 3 boxes of milk during weekdays
    saturday_boxes = 2 * weekday_boxes  # Lolita drinks twice the number of boxes on Saturdays than on weekdays
    sunday_boxes = 3 * weekday_boxes  # Lolita drinks thrice the number of boxes on Sundays than on weekdays

    # Calculate the total number of boxes of milk Lolita drinks per week
    total_boxes = (weekday_boxes * 5) + (saturday_boxes * 1) + (sunday_boxes * 1)
    result = total_boxes
    return result

print(solution())