def solution():
    """A window has 4 glass panels each. A house has 6 double windows downstairs and 8 single windows upstairs. How many glass panels are there in the whole house?"""
    # Define the number of glass panels per window
    panels_per_window = 4

    # Calculate the number of glass panels in the downstairs windows
    downstairs_glass = 6 * 2 * panels_per_window

    # Calculate the number of glass panels in the upstairs windows
    upstairs_glass = 8 * panels_per_window

    # Calculate the total number of glass panels
    total_glass = downstairs_glass + upstairs_glass

    # return the result
    result = total_glass
    return result

print(solution())