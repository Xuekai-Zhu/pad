def solution():
    """A window is made up of 8 glass panes. Each pane has a length of 12 inches and a width of 8 inches. What is the area of the window?"""
    # Define the length and width of each glass pane
    pane_length = 12
    pane_width = 8

    # Calculate the area of a single glass pane
    pane_area = pane_length * pane_width

    # Calculate the area of the entire window
    window_area = pane_area * 8

    result = window_area
    return result

print(solution())