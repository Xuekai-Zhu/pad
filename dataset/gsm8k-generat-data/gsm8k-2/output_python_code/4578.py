def solution():
    """A window is made up of 8 glass panes. Each pane has a length of 12 inches and a width of 8 inches. What is the area of the window?"""
    pane_length = 12
    pane_width = 8
    num_panes = 8
    pane_area = pane_length * pane_width
    window_area = pane_area * num_panes
    result = window_area
    return result

print(solution())