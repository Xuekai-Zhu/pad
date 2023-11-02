def solution():
    """James had two browsers on his computer. In each browser, he opened three windows, each with ten tabs. What's the total number of tabs he opened in all the browsers together?"""
    windows_per_browser = 3
    tabs_per_window = 10
    total_tabs_per_browser = windows_per_browser * tabs_per_window
    total_tabs = total_tabs_per_browser * 2
    result = total_tabs
    return result

print(solution())