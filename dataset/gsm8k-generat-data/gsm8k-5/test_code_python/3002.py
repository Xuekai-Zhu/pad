def solution():
    trays = 3  # Brenda needs to make 3 trays of banana pudding
    cookies_per_tray = 80  # Each tray needs 80 wafer cookies
    cookies_per_box = 60  # Each box of cookies contains 60 cookies
    boxes_per_tray = cookies_per_tray / cookies_per_box  # Brenda needs this many boxes to make one tray
    total_boxes = boxes_per_tray * trays  # Brenda needs this many boxes to make all the trays

    # Calculate the total cost of the boxes
    box_cost = 3.5  # Each box costs $3.50
    total_cost = total_boxes * box_cost
    result = total_cost
    return result

print(solution())