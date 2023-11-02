def solution():
    """Sophie does 4 loads of laundry a week and uses 1 dryer sheet per load. A box of dryer sheets costs $5.50 and has 104 dryer sheets in a box. On her birthday, she was given wool dryer balls to use instead of dryer sheets. How much money does she save in a year not buying dryer sheets?"""
    loads_per_week = 4
    sheets_per_load = 1
    sheets_per_box = 104
    cost_per_box = 5.50
    weeks_in_year = 52
    total_sheets_used = loads_per_week * weeks_in_year * sheets_per_load
    boxes_of_sheets_used = total_sheets_used / sheets_per_box
    cost_of_sheets_used = boxes_of_sheets_used * cost_per_box
    cost_of_wool_balls = 20
    money_saved = cost_of_sheets_used - cost_of_wool_balls
    result = money_saved
    return result

print(solution())