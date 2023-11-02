def solution():
    """A window has 4 glass panels each. A house has 6 double windows downstairs and 8 single windows upstairs. How many glass panels are there in the whole house?"""
    double_window_panels = 4 * 2
    single_window_panels = 4
    downstairs_windows = 6 * double_window_panels
    upstairs_windows = 8 * single_window_panels
    total_panels = downstairs_windows + upstairs_windows
    result = total_panels
    return result

print(solution())