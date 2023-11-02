def solution():
    """Brenda volunteered to make 3 trays of banana pudding for the family reunion. Each tray of banana pudding would need 80 wafer cookies. A box of wafer cookies only had 60 cookies per box. Each box costs $3.50. How much will it cost her to buy just enough boxes for 3 trays of banana pudding?"""
    cookies_per_tray = 80
    boxes_per_tray = cookies_per_tray / 60
    total_boxes = boxes_per_tray * 3
    box_cost = 3.5
    total_cost = total_boxes * box_cost
    result = total_cost
    return result

print(solution())