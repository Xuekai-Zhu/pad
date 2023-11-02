def solution():
    total_windows = 122  # There are 122 windows total
    four_window_rooms = 5  # 5 rooms have 4 windows each
    three_window_rooms = 8  # 8 rooms have 3 windows each

    # Calculate the total number of windows in rooms with 4 windows
    total_four_windows = four_window_rooms * 4

    # Calculate the total number of windows in rooms with 3 windows
    total_three_windows = three_window_rooms * 3

    # Calculate the total number of windows in rooms with 2 windows
    total_two_windows = total_windows - total_four_windows - total_three_windows

    # Calculate the number of rooms with 2 windows
    rooms_with_two_windows = total_two_windows / 2
    result = rooms_with_two_windows
    return result

print(solution())