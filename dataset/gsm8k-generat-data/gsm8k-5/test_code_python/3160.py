def solution():
    tabs_per_window = 10  # James opened 10 tabs in each window
    windows_per_browser = 3  # James opened 3 windows in each browser
    browsers = 2  # James had two browsers on his computer

    # Calculate the total number of tabs James opened
    total_tabs = tabs_per_window * windows_per_browser * browsers
    result = total_tabs
    return result

print(solution())