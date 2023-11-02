def solution():
    """Sophie does 4 loads of laundry a week and uses 1 dryer sheet per load. A box of dryer sheets costs $5.50 and has 104 dryer sheets in a box. On her birthday, she was given wool dryer balls to use instead of dryer sheets. How much money does she save in a year not buying dryer sheets?"""
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