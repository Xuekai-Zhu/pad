def solution():
    """A window has 4 glass panels each. A house has 6 double windows downstairs and 8 single windows upstairs. How many glass panels are there in the whole house?"""
    # Define the number of glass panels per window
    PANELS_PER_WINDOW = 4

    # Define the number of windows
    downstairs_windows = 6
    upstairs_windows = 8

    # Calculate the total number of glass panels
    total_panels = (2 * downstairs_windows * PANELS_PER_WINDOW) + (upstairs_windows * PANELS_PER_WINDOW)

    # Display the total number of glass panels
    result = total_panels
    return result

print(solution())