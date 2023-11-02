def solution():
    
    total_windows = 122
    four_window_rooms = 5
    three_window_rooms = 8
    total_four_windows = four_window_rooms * 4
    total_three_windows = three_window_rooms * 3
    total_two_windows = total_windows - total_four_windows - total_three_windows
    num_two_window_rooms = total_two_windows // 2
    result = num_two_window_rooms
    return result

print(solution())