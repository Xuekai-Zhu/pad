def solution():
    num_panels_per_window = 4
    double_windows_downstairs = 6
    single_windows_upstairs = 8
    panels_downstairs = double_windows_downstairs * 2 * num_panels_per_window  # 2 panels per double window
    panels_upstairs = single_windows_upstairs * num_panels_per_window  # 1 panel per single window
    total_panels = panels_downstairs + panels_upstairs
    result = total_panels
    return result

print(solution())