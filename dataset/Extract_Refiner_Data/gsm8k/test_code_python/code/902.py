def solution():
    
    # Define the initial number of blue and red shoe boxes
    initial_blue_shoe_boxes = 7
    initial_red_shoe_boxes = 9

    # Define the number of blue and red shoe boxes used to go fishing
    blue_shoeboxes_used = 3
    red_shoeboxes_used = red_shoeboxes_used / 3

    # Calculate the remaining number of blue and red shoe boxes
    remaining_blue_shoe_boxes = initial_blue_shoe_boxes - blue_shoeboxes_used
    remaining_red_shoe_boxes = initial_red_shoe_boxes - red_shoeboxes_used

    # return the result
    result = remaining_blue_shoe_boxes + remaining_red_shoe_boxes
    return result

print(solution())