def solution():
    glass_panels_per_window = 4  # Each window has 4 glass panels
    double_windows_downstairs = 6  # There are 6 double windows downstairs
    single_windows_upstairs = 8  # There are 8 single windows upstairs

    # Calculate the total number of glass panels in the downstairs windows
    downstairs_glass_panels = double_windows_downstairs * 2 * glass_panels_per_window

    # Calculate the total number of glass panels in the upstairs windows
    upstairs_glass_panels = single_windows_upstairs * glass_panels_per_window

    # Calculate the total number of glass panels in the whole house
    total_glass_panels = downstairs_glass_panels + upstairs_glass_panels
    result = total_glass_panels
    return result

print(solution())