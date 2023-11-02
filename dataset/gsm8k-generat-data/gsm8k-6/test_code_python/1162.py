def solution():
    # Calculate the number of granola bars left after Monroe and her husband ate 80
    remaining_bars = 200 - 80

    # Calculate the number of children in the family
    num_children = remaining_bars // 20  # each child received 20 granola bars

    result = num_children
    return result

print(solution())