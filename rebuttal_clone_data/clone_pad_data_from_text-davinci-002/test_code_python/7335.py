def solution():
    loads_per_week = 4
    weeks_per_year = 52
    dryer_sheets_per_load = 1
    dryer_sheets_per_box = 104
    boxes_per_year = loads_per_week * weeks_per_year / dryer_sheets_per_box
    cost_per_box = 5.50
    total_cost = boxes_per_year * cost_per_box
    result = total_cost
    return result

print(solution())