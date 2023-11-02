def solution():
    times_played = 3
    boxes_per_game = 3
    cost_per_box = 25

    # Calculate the total number of boxes of paintballs John buys in a month
    total_boxes = times_played * boxes_per_game

    # Calculate the total cost of all boxes of paintballs John buys in a month
    total_cost = total_boxes * cost_per_box
    result = total_cost
    return result

print(solution())