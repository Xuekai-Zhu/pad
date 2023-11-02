def solution():
    
    # Define the initial number of blue and red shoe boxes
    blue_boxes = 7
    red_boxes = 9

    # Define the number of blue and red shoe boxes used to go fishing
    blue_boxes_used = 3
    red_boxes_used = red_boxes_used / 3

    # Calculate the number of blue and red shoe boxes left
    blue_boxes_left = blue_boxes - blue_boxes_used
    red_boxes_left = red_boxes - red_boxes_used

    # Display the number of red and blue shoe boxes left
    result = red_boxes_left
    return result

print(solution())