def solution():
    """Jose had 400 tabs opened up in his windows browser. After about one hour of browsing, he closed 1/4 of the tabs to allows easy browsing. He read some news from different pages, then closed 2/5 of the remaining tabs. If he closed half of the remaining tabs after further analyzing some pages, how many windows tabs did he have remaining open?"""
    initial_tabs = 400
    first_closing = initial_tabs / 4
    remaining_tabs = initial_tabs - first_closing
    second_closing = remaining_tabs * (2 / 5)
    remaining_tabs = remaining_tabs - second_closing
    final_closing = remaining_tabs / 2
    
    result = remaining_tabs - final_closing
    return result

print(solution())