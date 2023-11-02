def solution():
    gallons_per_box = 30
    cost_per_box = 40
    weekly_gallons = 180
    
    # Calculate the number of boxes needed per week
    boxes_per_week = weekly_gallons / gallons_per_box
    
    # Calculate the total cost of syrup per week
    cost_per_week = boxes_per_week * cost_per_box
    result = cost_per_week
    return result

print(solution())