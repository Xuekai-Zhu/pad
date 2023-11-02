def solution():
    # Calculate the number of tabs remaining open after each step
    remaining_tabs = 400 - (1/4 * 400)  # Jose closes 1/4 of the tabs
    remaining_tabs = remaining_tabs - (2/5 * remaining_tabs)  # Jose closes 2/5 of the remaining tabs
    remaining_tabs = remaining_tabs / 2  # Jose closes half of the remaining tabs

    result = remaining_tabs
    return result

print(solution())