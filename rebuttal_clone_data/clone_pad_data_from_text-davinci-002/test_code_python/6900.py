def solution():
    panels_per_window = 4
    double_windows = 6
    single_windows = 8
    total_windows = double_windows + single_windows
    total_panels = panels_per_window * total_windows
    result = total_panels
    return result

print(solution())