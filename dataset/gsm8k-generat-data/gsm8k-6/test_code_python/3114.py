def solution():
    # Calculate the total number of boxes sold by Jill
    total_boxes = 5 + 4*5 + (4*5)/2 + 3*(4*5)/2 + 10  # first customer buys 5 boxes, second buys 20, third buys 10, fourth buys 30, last customer buys 10
    boxes_left = 150 - total_boxes  # calculate the number of boxes left to hit Jill's sales goal
    result = boxes_left
    return result

print(solution())