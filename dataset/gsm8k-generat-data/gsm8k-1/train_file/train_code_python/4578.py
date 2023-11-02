def solution():
    """A window is made up of 8 glass panes. Each pane has a length of 12 inches and a width of 8 inches. What is the area of the window?"""
    num_panes = 8
    length = 12
    width = 8
    pane_area = length * width
    window_area = num_panes * pane_area
    result = window_area
    return result

print(solution())