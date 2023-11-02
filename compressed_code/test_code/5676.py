def solution():
    
    loads_per_week = 4
    dryer_sheets_per_load = 1
    cost_per_box = 5.5
    sheets_per_box = 104
    weeks_per_year = 52
    dryer_sheets_per_year = loads_per_week * dryer_sheets_per_load * weeks_per_year
    boxes_per_year = dryer_sheets_per_year / sheets_per_box
    cost_saved_per_year = boxes_per_year * cost_per_box
    result = cost_saved_per_year
    return result

print(solution())