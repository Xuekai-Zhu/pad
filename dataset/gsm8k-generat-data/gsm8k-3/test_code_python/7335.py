def solution():
    """Sophie does 4 loads of laundry a week and uses 1 dryer sheet per load.  A box of dryer sheets costs $5.50 and has 104 dryer sheets in a box.  On her birthday, she was given wool dryer balls to use instead of dryer sheets.  How much money does she save in a year not buying dryer sheets?"""
    # Define the number of loads of laundry Sophie does in a week and the cost of a box of dryer sheets
    LAUNDRY_LOADS_PER_WEEK = 4
    DRYER_SHEET_COST_PER_BOX = 5.50
    DRYER_SHEET_COUNT_PER_BOX = 104

    # Calculate the number of dryer sheets Sophie uses in a week and in a year
    dryer_sheets_per_week = LAUNDRY_LOADS_PER_WEEK
    dryer_sheets_per_year = dryer_sheets_per_week * 52

    # Calculate the number of boxes of dryer sheets Sophie would need to buy in a year
    boxes_of_dryer_sheets_per_year = dryer_sheets_per_year / DRYER_SHEET_COUNT_PER_BOX
    boxes_of_dryer_sheets_per_year = math.ceil(boxes_of_dryer_sheets_per_year)

    # Calculate the cost of buying that many boxes of dryer sheets in a year
    cost_of_dryer_sheets_per_year = boxes_of_dryer_sheets_per_year * DRYER_SHEET_COST_PER_BOX

    # Display the money Sophie saves in a year by not buying dryer sheets
    result = cost_of_dryer_sheets_per_year
    return result

print(solution())