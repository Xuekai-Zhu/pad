def solution():
    """James had two browsers on his computer. In each browser, he opened three windows, each with ten tabs. What's the total number of tabs he opened in all the browsers together?"""
    windows_per_browser = 3
    tabs_per_window = 10
    total_browsers = 2
    total_tabs = windows_per_browser * tabs_per_window * total_browsers
    result = total_tabs
    return result

print(solution())