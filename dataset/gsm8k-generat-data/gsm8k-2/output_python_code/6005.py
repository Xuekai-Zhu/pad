def solution():
    """Jose had 400 tabs opened up in his windows browser. After about one hour of browsing, he closed 1/4 of the tabs to allows easy browsing. He read some news from different pages, then closed 2/5 of the remaining tabs. If he closed half of the remaining tabs after further analyzing some pages, how many windows tabs did he have remaining open?"""
    total_tabs = 400
    first_close = total_tabs * 0.25
    remaining_tabs = total_tabs - first_close
    second_close = remaining_tabs * 0.4
    remaining_tabs -= second_close
    third_close = remaining_tabs / 2
    remaining_tabs -= third_close
    result = remaining_tabs
    return result

print(solution())