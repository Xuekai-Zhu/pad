def solution():
    """Farrah ordered 4 boxes from Amazon containing 20 matchboxes each. If each matchbox has 300 sticks, calculate the total number of match sticks that Farah ordered?"""
    boxes = 4
    matchboxes_per_box = 20
    sticks_per_matchbox = 300
    total_sticks = boxes * matchboxes_per_box * sticks_per_matchbox
    result = total_sticks
    return result

print(solution())