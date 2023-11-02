def solution():
    # Calculate the total number of windows in 4-window rooms
    four_window_total = 5 * 4

    # Calculate the total number of windows in 3-window rooms
    three_window_total = 8 * 3

    # Calculate the total number of windows in the building
    total_windows = four_window_total + three_window_total

    # Calculate the difference between the total number of windows and the known windows
    # and divide by 2 to get the total number of 2-window rooms
    two_window_total = (122 - total_windows) / 2

    result = two_window_total
    return result

print(solution())