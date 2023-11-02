def solution():
    total_bars = 200  # Monroe made 200 granola bars
    bars_eaten = 80  # Monroe and her husband ate 80 bars
    bars_left = total_bars - bars_eaten  # The number of bars left for the children

    # Calculate the number of children
    num_children = bars_left / 20
    result = num_children
    return result

print(solution())