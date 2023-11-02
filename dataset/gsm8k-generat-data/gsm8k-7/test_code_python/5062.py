def solution():
    num_total_windows = 122
    num_rooms_with_4_windows = 5
    num_rooms_with_3_windows = 8

    # Calculate the total number of windows in rooms with 4 windows
    total_windows_with_4 = num_rooms_with_4_windows * 4

    # Calculate the total number of windows in rooms with 3 windows
    total_windows_with_3 = num_rooms_with_3_windows * 3

    # Calculate the total number of windows in rooms with 2 windows
    total_windows_with_2 = num_total_windows - total_windows_with_4 - total_windows_with_3

    # Calculate the number of rooms with 2 windows
    num_rooms_with_2_windows = total_windows_with_2 / 2
    result = num_rooms_with_2_windows
    return result

print(solution())