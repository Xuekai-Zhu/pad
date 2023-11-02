def solution():
    total_windows = 122
    windows_in_5_rooms = 4*5
    windows_in_8_rooms = 3*8
    windows_in_2_rooms = total_windows - (windows_in_5_rooms + windows_in_8_rooms)
    result = windows_in_2_rooms / 2
    return result

print(solution())