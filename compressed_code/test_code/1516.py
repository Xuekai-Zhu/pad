def solution():
    
    normal_mouse_cost = 120
    left_handed_mouse_cost = normal_mouse_cost * 1.3
    num_left_handed_mice = 25
    num_days_open = 7 - 3  
    total_mice_sold = num_left_handed_mice * num_days_open
    total_sales = total_mice_sold * left_handed_mouse_cost
    result = total_sales
    return result

print(solution())