def solution():
    """Brenda volunteered to make 3 trays of banana pudding for the family reunion. Each tray of banana pudding would need 80 wafer cookies. A box of wafer cookies only had 60 cookies per box. Each box costs $3.50. How much will it cost her to buy just enough boxes for 3 trays of banana pudding?"""
    cookies_per_tray = 80
    trays = 3
    cookies_per_box = 60
    boxes_needed = ((cookies_per_tray * trays) // cookies_per_box) + 1
    cost_per_box = 3.50
    total_cost = boxes_needed * cost_per_box
    result = total_cost
    return result

print(solution())