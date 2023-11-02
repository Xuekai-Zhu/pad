def solution():
    """Monroe made 200 granola bars for her family. She and her husband ate 80, and the rest was divided equally among her children. If each child received 20 granola bars, how many children are in the family?"""
    total_bars = 200
    bars_eaten = 80
    bars_left = total_bars - bars_eaten
    child_bars = 20
    num_children = bars_left / child_bars
    result = num_children
    return result

print(solution())