def solution():
    loads_per_week = 4
    dryer_sheets_per_load = 1
    box_cost = 5.5
    sheets_per_box = 104

    # Calculate the number of dryer sheets Sophie uses in a year
    sheets_per_year = loads_per_week * dryer_sheets_per_load * 52

    # Calculate how many boxes of dryer sheets Sophie would need to buy in a year
    boxes_per_year = sheets_per_year // sheets_per_box + 1  # Round up to nearest box

    # Calculate the total cost of buying dryer sheets in a year
    total_cost_with_sheets = boxes_per_year * box_cost

    # Assume Sophie uses wool dryer balls indefinitely (no need to repurchase)
    total_cost_with_balls = 0

    # Calculate how much money Sophie saves in a year by using wool dryer balls instead of dryer sheets
    savings_per_year = total_cost_with_sheets - total_cost_with_balls
    result = savings_per_year
    return result

print(solution())