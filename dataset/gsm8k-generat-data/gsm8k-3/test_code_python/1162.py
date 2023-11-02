def solution():
    """Monroe made 200 granola bars for her family. She and her husband ate 80, and the rest was divided equally among her children. If each child received 20 granola bars, how many children are in the family?"""
    # Define the total number of granola bars made
    total_bars = 200

    # Subtract the number of bars eaten by Monroe and her husband
    remaining_bars = total_bars - 80

    # Divide the remaining bars equally among the children
    child_bars = 20
    num_children = remaining_bars // child_bars

    # Display the number of children
    result = num_children
    return result

print(solution())