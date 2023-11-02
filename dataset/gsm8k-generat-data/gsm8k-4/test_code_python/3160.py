def solution():
    """James had two browsers on his computer. In each browser, he opened three windows, each with ten tabs. What's the total number of tabs he opened in all the browsers together?"""
    # Define the number of windows per browser and the number of tabs per window
    windows_per_browser = 3
    tabs_per_window = 10

    # Calculate the total number of tabs opened in one browser
    tabs_per_browser = windows_per_browser * tabs_per_window

    # Calculate the total number of tabs opened in both browsers
    total_tabs = tabs_per_browser * 2

    # return the result
    result = total_tabs
    return result

print(solution())