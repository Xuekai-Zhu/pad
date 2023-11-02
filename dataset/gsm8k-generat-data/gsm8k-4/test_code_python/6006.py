def solution():
    """Jose had 400 tabs opened up in his windows browser. After about one hour of browsing, he closed 1/4 of the tabs to allows easy browsing. He read some news from different pages, then closed 2/5 of the remaining tabs. If he closed half of the remaining tabs after further analyzing some pages, how many windows tabs did he have remaining open?"""
    # Define the initial number of tabs
    initial_tabs = 400

    # Calculate the number of tabs after closing 1/4 of them
    tabs_after_first_close = initial_tabs * 0.75

    # Calculate the number of tabs after closing 2/5 of the remaining tabs
    tabs_after_second_close = tabs_after_first_close * 0.6

    # Calculate the number of tabs after closing half of the remaining tabs
    tabs_after_third_close = tabs_after_second_close * 0.5

    # Return the final number of remaining tabs
    result = tabs_after_third_close
    return result

print(solution())