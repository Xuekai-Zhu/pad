def solution():
    loads_per_week = 4
    sheets_per_load = 1
    cost_per_box = 5.50
    sheets_per_box = 104

    # Calculate the number of dryer sheets used in a year
    sheets_per_year = loads_per_week * 52 * sheets_per_load

    # Calculate the number of boxes of dryer sheets needed in a year
    boxes_per_year = sheets_per_year / sheets_per_box

    # Calculate the total cost of dryer sheets in a year
    cost_per_year = boxes_per_year * cost_per_box

    # Assume wool dryer balls last for 2 years and don't require replacement
    wool_balls_cost = cost_per_box * 2
    total_savings = cost_per_year - wool_balls_cost
    
    return total_savings

print(solution())