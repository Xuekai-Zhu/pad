def solution():
    """Every room in a building has at least two windows and a maximum of 4 windows. There are 122 windows total. If 5 rooms have 4 windows and 8 rooms have 3 windows, how many rooms in the building have 2 windows?"""
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