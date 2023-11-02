def solution():
    """A window has 4 glass panels each. A house has 6 double windows downstairs and 8 single windows upstairs. How many glass panels are there in the whole house?"""
    glass_per_window = 4
    downstairs_windows = 6 * 2
    upstairs_windows = 8
    total_windows = downstairs_windows + upstairs_windows
    total_glass_panels = total_windows * glass_per_window
    result = total_glass_panels
    return result

print(solution())