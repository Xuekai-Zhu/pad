def solution():
    """Katie's mother wants to get granola bars for all the kids to eat after Katie's soccer game. There will be 30 kids playing soccer, including Katie. Katie's mother wants to get 2 granola bars for each kid, since the bars are not that big and she figures the kids will be very hungry. Each box of granola bars has 12 bars in it. How many boxes should Katie's mother buy?"""
    total_kids = 30
    bars_per_kid = 2
    bars_per_box = 12
    total_bars = total_kids * bars_per_kid
    boxes_needed = total_bars / bars_per_box
    result = boxes_needed
    
    return result

print(solution())