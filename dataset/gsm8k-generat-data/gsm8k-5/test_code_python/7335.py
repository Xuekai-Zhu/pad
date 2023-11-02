def solution():
    loads_per_week = 4  # Sophie does 4 loads of laundry a week
    dryer_sheets_per_load = 1  # Sophie uses 1 dryer sheet per load
    dryer_sheets_per_box = 104  # A box of dryer sheets has 104 sheets
    cost_per_box = 5.50  # A box of dryer sheets costs $5.50
    weeks_per_year = 52  # There are 52 weeks in a year

    # Calculate the number of boxes of dryer sheets Sophie buys per year
    boxes_per_year = (loads_per_week * dryer_sheets_per_load * weeks_per_year) / dryer_sheets_per_box

    # Calculate the amount of money Sophie saves by using wool dryer balls instead of dryer sheets
    savings_per_year = boxes_per_year * cost_per_box
    result = savings_per_year
    return result

print(solution())