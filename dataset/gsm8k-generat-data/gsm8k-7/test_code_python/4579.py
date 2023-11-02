def solution():
    num_panes = 8
    length = 12
    width = 8

    # Calculate the area of one pane
    pane_area = length * width

    # Calculate the total area of all panes
    total_area = pane_area * num_panes
    result = total_area
    return result

print(solution())