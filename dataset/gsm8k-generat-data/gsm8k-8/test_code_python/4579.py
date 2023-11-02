def solution():
    pane_length = 12 # inches
    pane_width = 8 # inches
    num_panes = 8
    area_per_pane = pane_length * pane_width # square inches

    total_area = num_panes * area_per_pane # square inches
    result = total_area
    return result

print(solution())