def solution():
    # Define the number of windows and tabs per browser
    windows_per_browser = 3
    tabs_per_window = 10

    # Calculate the total number of tabs
    total_tabs = windows_per_browser * tabs_per_window * 2
    result = total_tabs
    return result

print(solution())