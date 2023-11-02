def solution():
    """Sophie does 4 loads of laundry a week and uses 1 dryer sheet per load. A box of dryer sheets costs $5.50 and has 104 dryer sheets in a box. On her birthday, she was given wool dryer balls to use instead of dryer sheets. How much money does she save in a year not buying dryer sheets?"""
    # Define the number of loads of laundry done per week and the number of dryer sheets used per load
    laundry_per_week = 4
    dryer_sheets_per_load = 1

    # Define the cost of a box of dryer sheets and the number of dryer sheets in a box
    dryer_sheet_cost = 5.50
    dryer_sheets_per_box = 104

    # Calculate the number of dryer sheets used in a year
    dryer_sheets_per_year = laundry_per_week * dryer_sheets_per_load * 52

    # Calculate the number of boxes of dryer sheets needed in a year
    boxes_per_year = dryer_sheets_per_year / dryer_sheets_per_box

    # Calculate the cost of buying the necessary number of boxes of dryer sheets in a year
    cost_of_dryer_sheets = boxes_per_year * dryer_sheet_cost

    # Calculate the cost of buying wool dryer balls once
    cost_of_wool_balls = 10

    # Calculate the total savings in a year by using wool dryer balls instead of dryer sheets
    total_savings = cost_of_dryer_sheets - cost_of_wool_balls

    result = total_savings
    return result

print(solution())