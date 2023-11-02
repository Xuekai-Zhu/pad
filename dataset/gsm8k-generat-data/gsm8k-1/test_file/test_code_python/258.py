def solution():
    """Maddison has 5 boxes with 50 marbles in each box. Then she gets 20 marbles from her friend. How many marbles does she have now?"""
    marbles_per_box = 50
    num_boxes = 5
    initial_marbles = marbles_per_box * num_boxes
    extra_marbles = 20
    total_marbles = initial_marbles + extra_marbles
    result = total_marbles
    return result

print(solution())