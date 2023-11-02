def solution():
    total_boxes = 150  # total boxes sold on both days
    sunday_boxes = 1.5 * saturday_boxes  # Sunday sales are 50% more than Saturday sales
    saturday_boxes = (total_boxes - sunday_boxes) / 2  # Calculate Saturday sales by subtracting Sunday sales from total sales and dividing by 2
    result = saturday_boxes
    return result

print(solution())