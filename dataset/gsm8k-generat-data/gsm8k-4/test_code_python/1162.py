def solution():
    """Monroe made 200 granola bars for her family. She and her husband ate 80, and the rest was divided equally among her children. If each child received 20 granola bars, how many children are in the family?"""
    # Define the total number of granola bars and the number eaten by Monroe and her husband
    total_bars = 200
    eaten_bars = 80

    # Calculate the number of bars left for the children
    children_bars = total_bars - eaten_bars

    # Calculate the number of children based on the number of bars each received
    num_children = children_bars // 20

    # return the result
    result = num_children
    return result

print(solution())