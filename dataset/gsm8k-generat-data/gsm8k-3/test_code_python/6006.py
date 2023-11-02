def solution():
    """Jose had 400 tabs opened up in his windows browser. After about one hour of browsing, he closed 1/4 of the tabs to allows easy browsing. He read some news from different pages, then closed 2/5 of the remaining tabs. If he closed half of the remaining tabs after further analyzing some pages, how many windows tabs did he have remaining open?"""
    # Define the starting number of tabs
    starting_tabs = 400

    # Calculate the number of tabs remaining after closing 1/4 of the starting tabs
    tabs_after_first_close = starting_tabs * (3/4)

    # Calculate the number of tabs remaining after closing 2/5 of the remaining tabs
    tabs_after_second_close = tabs_after_first_close * (3/5)

    # Calculate the number of tabs remaining after closing half of the remaining tabs
    tabs_after_third_close = tabs_after_second_close * (1/2)

    # Display the number of tabs remaining
    result = tabs_after_third_close
    return result

print(solution())