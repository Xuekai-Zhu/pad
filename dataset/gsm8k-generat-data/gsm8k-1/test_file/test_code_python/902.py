def solution():
    """Tim has a box with 7 blue shoe boxes and 9 red shoe boxes. If he uses 3 blue shoeboxes and 1/3 red of his shoeboxes to go fishing, how many red and blue shoe boxes are left in Tim's box?"""
    
    # Total number of shoe boxes
    total_boxes = 7 + 9
    
    # Number of blue shoe boxes left after going fishing
    blue_left = 7 - 3
    
    # Number of red shoe boxes left after going fishing
    red_left = round(9 - (1/3)*9)
    
    # Total number of shoe boxes left
    total_left = blue_left + red_left
    
    result = (blue_left, red_left)
    
    return result

print(solution())