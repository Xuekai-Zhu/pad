def solution():
    # Define the initial number of tabs
    initial_tabs = 400

    # Calculate the number of tabs after closing 1/4 of them
    tabs_after_first_close = initial_tabs - (1/4)*initial_tabs

    # Calculate the number of tabs after closing 2/5 of the remaining tabs
    tabs_after_second_close = tabs_after_first_close - (2/5)*(tabs_after_first_close)

    # Calculate the number of tabs after closing half of the remaining tabs
    tabs_after_third_close = tabs_after_second_close - 0.5*(tabs_after_second_close)

    result = tabs_after_third_close
    return result

print(solution())