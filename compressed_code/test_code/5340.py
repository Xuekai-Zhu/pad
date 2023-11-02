def solution():
    
    double_window_panels = 4 * 2
    single_window_panels = 4
    downstairs_windows = 6 * double_window_panels
    upstairs_windows = 8 * single_window_panels
    total_panels = downstairs_windows + upstairs_windows
    result = total_panels
    return result

print(solution())