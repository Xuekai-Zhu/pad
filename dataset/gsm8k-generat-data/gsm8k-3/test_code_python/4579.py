def solution():
    """A window is made up of 8 glass panes. Each pane has a length of 12 inches and a width of 8 inches. What is the area of the window?"""
    # Define the length and width of each pane
    LENGTH = 12
    WIDTH = 8

    # Calculate the area of each pane
    pane_area = LENGTH * WIDTH

    # Calculate the total area of the window
    total_area = pane_area * 8

    # Display the total area of the window
    result = total_area
    return result

print(solution())