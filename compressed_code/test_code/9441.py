def solution():
    
    money_saved_per_week = 15
    weeks_to_fill_box = 60
    total_savings_per_box = money_saved_per_week * weeks_to_fill_box
    num_boxes = 5
    total_savings = total_savings_per_box * num_boxes
    result = total_savings
    return result

print(solution())