def solution():
    # Calculate the total number of tabs James opened
    tabs_per_window = 10
    windows_per_browser = 3
    browsers = 2 
    total_tabs = tabs_per_window * windows_per_browser * browsers
    result = total_tabs
    return result

print(solution())