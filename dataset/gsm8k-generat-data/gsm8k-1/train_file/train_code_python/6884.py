def solution():
    """Farrah ordered 4 boxes from Amazon containing 20 matchboxes each. If each matchbox has 300 sticks, calculate the total number of match sticks that Farah ordered?"""
    num_boxes = 4
    num_matchboxes = 20
    num_sticks_per_matchbox = 300
    total_sticks = num_boxes * num_matchboxes * num_sticks_per_matchbox
    result = total_sticks
    return result

print(solution())