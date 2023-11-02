def solution():
    """James had two browsers on his computer. In each browser, he opened three windows, each with ten tabs. What's the total number of tabs he opened in all the browsers together?"""
    # Define the number of windows and tabs per window
    WINDOWS_PER_BROWSER = 3
    TABS_PER_WINDOW = 10

    # Calculate the total number of tabs opened in one browser
    tabs_per_browser = WINDOWS_PER_BROWSER * TABS_PER_WINDOW

    # Calculate the total number of tabs opened in both browsers
    total_tabs = tabs_per_browser * 2

    # Display the total number of tabs
    result = total_tabs
    return result

print(solution())