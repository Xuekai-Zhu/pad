def solution():
    num_browsers = 2
    num_windows_per_browser = 3
    num_tabs_per_window = 10

    # Calculate the total number of tabs opened in one browser
    tabs_per_browser = num_windows_per_browser * num_tabs_per_window

    # Calculate the total number of tabs opened in both browsers
    total_tabs = num_browsers * tabs_per_browser
    result = total_tabs
    return result

print(solution())